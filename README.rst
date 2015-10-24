How to build alignak packages
=============================

Debian/Ubuntu 
=============

::

   apt-get install debhelper git-buildpackage python-pbr quilt
   git clone https://github.com/Alignak-monitoring/alignak.git ~/alignak
   git clone https://github.com/Alignak-monitoring/alignak-packaging.git ~/alignak-packaging
   cp -r ~/alignak-packaging/debian ~/alignak-packaging/manpages ~/alignak
   cd ~/alignak
   # You will package current develop here, if you need master or specific checkout what you need
   # You could just use `git-buildpackage -us -uc -tc -b` here but you have to add and commit the new file added
   # This commit can't be pushed upstream of course
  
   RELEASE=$(git log -1  --format=%ct.%h)
   cd ../
   VERSION=$(awk -F'\(?\-?' '/alignak/ {print $2}' alignak/debian/changelog)
   sed -i "s/-\([0-9]\+\))/-\1.$RELEASE)/g" alignak/debian/changelog
   tar -czf alignak_$VERSION.orig.tar.gz alignak
   cd alignak
   dpkg-buildpackage
   lintian ../alignak*.deb

Fedora/RedHat/CentOs
====================

::
   yum install rpm-build git python-pbr python-devel
   git clone https://github.com/Alignak-monitoring/alignak.git ~/alignak
   git clone https://github.com/Alignak-monitoring/alignak-packaging.git ~/alignak-packaging
   cp -r ~/alignak-packaging/debian ~/alignak-packaging/manpages ~/alignak
   # You will package current develop here, if you need master or specific checkout what you need 
   cd ~/alignak
   RELEASE=$(git log -1  --format=%ct_%h)
   cd ../
   VERSION=$(awk '/Version/ {print $2}' ~/alignak-packaging/alignak.spec)
   sed -i "s/\(Release:.*\)$/\1_$RELEASE/g" ~/alignak-packaging/alignak.spec
   mkdir -p ~/rpmbuild/SOURCES
   tar -czf ~/rpmbuild/SOURCES/alignak-$VERSION.tar.gz alignak
   rpmbuild -ba  ~/alignak-packaging/alignak.spec
   rpmlint ~rpmbuild/RPMS/x86_64/*.rpm



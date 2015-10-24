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
   git-buildpackage -us -uc -tc -b


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
   sed -i "s/\(Release:.*\)$/\1_$VERSION/g" ~/alignak-packaging/alignak.spec
   mkdir -p ~/rpmbuild/SOURCES
   tar -czf ~/rpmbuild/SOURCES/alignak-$VERSION.tar.gz alignak
   rpmbuild -ba  ~/alignak-packaging/alignak.spec
   rpmlint ~rpmbuild/RPMS/x86_64/*.rpm



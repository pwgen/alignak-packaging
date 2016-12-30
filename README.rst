How to build alignak packages
=============================

**Note**: The content of some folders (*debian*, *manpages* and *systemd*) of this repository is copied in the alignak repository. The resulting alignak folder is a superimposition of both repositories that will be used to build the installer packages.

The recommended way to build Alignak packages is to to use the scripts existing in the `Alignak docker`_ repository.

.. _Alignak docker: https://github.com/Alignak-monitoring/alignak-docker

The following example scripts simply allow to build packages for testing purpose.

Debian/Ubuntu 
=============

::

    # Install required packages for building
    apt-get install -y debhelper git-buildpackage python-pbr quilt vim lsb-release

    # Get alignak and packaging repos
    git clone https://github.com/Alignak-monitoring/alignak.git ~/alignak
    # You will package the current develop branch here, if you need master or other,
    # checkout what you need from the repository

    git clone https://github.com/Alignak-monitoring/alignak-packaging.git ~/alignak-packaging

    # Update alignak repo with packaging files (debian, manpages, systemd and systemV)
    cp -r ~/alignak-packaging/debian ~/alignak-packaging/manpages ~/alignak-packaging/systemd ~/alignak-packaging/systemV ~/alignak

    # Build an archive from the repository
    # Set the correct current version number, else the build with fail...
    VERSION=0.2
    tar -czf alignak_$VERSION.orig.tar.gz alignak

    cd alignak
    # Build the package
    dpkg-buildpackage

    # Check package compliance
    lintian ../alignak*.deb


Fedora/RedHat/CentOs
====================

Not sure this part is up-to-date. to be confirmed?
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



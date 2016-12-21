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
    # Set the correct current version numer, else the build with fail...
    VERSION=0.2
    tar -czf alignak_$VERSION.orig.tar.gz alignak

    cd alignak
    dpkg-buildpackage
        # Output:
            dpkg-buildpackage: source package alignak
            dpkg-buildpackage: source version 0.2-1
            dpkg-buildpackage: source distribution unstable
            dpkg-buildpackage: source changed by Sebastien Coavoux <debian@pyseb.cx>
            dpkg-buildpackage: host architecture amd64
             dpkg-source --before-build alignak
             fakeroot debian/rules clean
            dh clean --with python2 --install-layout=deb,quilt
               dh_testdir -O--install-layout=deb,quilt
               dh_auto_clean -O--install-layout=deb,quilt

            # ---
            # Fred: From the get_init_scripts function of install_hooks.cfg
            Installable directories/files: ['']
            Installable directories/files: ['alignak ', '']
            Installable directories/files: ['alignak/log ', '']
            Installable directories/files: ['alignak/run ', '']
            Installable directories/files: ['alignak/libexec ', '']
            Installable directories/files: ['alignak/etc ', ' etc/*']
            Installable directories/files: ['alignak/bin/etc/init.d ', ' systemV/init.d/*']
            Installable directories/files: ['alignak/bin/etc/default ', ' systemV/default/alignak.in']
            Installable directories/files: ['alignak/etc ', ' systemV/alignak.ini']
            # ---

            running clean
            'build/lib.linux-x86_64-2.7' does not exist -- can't clean it
            'build/bdist.linux-x86_64' does not exist -- can't clean it
            'build/scripts-2.7' does not exist -- can't clean it
               debian/rules override_dh_clean
            make[1]: Entering directory '/home/alignak/alignak'
            rm -rf ./build
            rm -rf ./Alignak.egg-info
            dh_clean
            make[1]: Leaving directory '/home/alignak/alignak'
             dpkg-source -b alignak
            dpkg-source: info: using source format `3.0 (quilt)'
            dpkg-source: info: building alignak using existing ./alignak_0.2.orig.tar.gz
            dpkg-source: info: building alignak in alignak_0.2-1.debian.tar.xz
            dpkg-source: info: building alignak in alignak_0.2-1.dsc
             debian/rules build
            dh build --with python2 --install-layout=deb,quilt
               dh_testdir -O--install-layout=deb,quilt
               dh_auto_configure -O--install-layout=deb,quilt
               dh_auto_build -O--install-layout=deb,quilt
            Installable directories/files: ['']
            Installable directories/files: ['alignak ', '']
            Installable directories/files: ['alignak/log ', '']
            Installable directories/files: ['alignak/run ', '']
            Installable directories/files: ['alignak/libexec ', '']
            Installable directories/files: ['alignak/etc ', ' etc/*']
            Installable directories/files: ['alignak/bin/etc/init.d ', ' systemV/init.d/*']
            Installable directories/files: ['alignak/bin/etc/default ', ' systemV/default/alignak.in']
            Installable directories/files: ['alignak/etc ', ' systemV/alignak.ini']
            running build
            running build_py
            creating build
            creating build/lib.linux-x86_64-2.7
            creating build/lib.linux-x86_64-2.7/alignak
            copying alignak/external_command.py -> build/lib.linux-x86_64-2.7/alignak
            copying alignak/borg.py -> build/lib.linux-x86_64-2.7/alignak
            copying alignak/alignakobject.py -> build/lib.linux-x86_64-2.7/alignak
            ...
            ...
            ...
            copying alignak/bin/alignak_reactionner.py -> build/lib.linux-x86_64-2.7/alignak/bin
            copying alignak/bin/alignak_receiver.py -> build/lib.linux-x86_64-2.7/alignak/bin
            copying alignak/bin/alignak_scheduler.py -> build/lib.linux-x86_64-2.7/alignak/bin
            running egg_info
            creating alignak.egg-info
            writing requirements to alignak.egg-info/requires.txt
            writing alignak.egg-info/PKG-INFO
            writing top-level names to alignak.egg-info/top_level.txt
            writing dependency_links to alignak.egg-info/dependency_links.txt
            writing entry points to alignak.egg-info/entry_points.txt
            [pbr] Processing SOURCES.txt
            writing manifest file 'alignak.egg-info/SOURCES.txt'
            [pbr] In git context, generating filelist from git
            warning: no files found matching 'ChangeLog'
            warning: no previously-included files found matching '.gitreview'
            warning: no previously-included files matching '*.pyc' found anywhere in distribution
            writing manifest file 'alignak.egg-info/SOURCES.txt'
               dh_auto_test -O--install-layout=deb,quilt
             fakeroot debian/rules binary
            dh binary --with python2 --install-layout=deb,quilt
               dh_testroot -O--install-layout=deb,quilt
               dh_prep -O--install-layout=deb,quilt
               debian/rules override_dh_installdirs
            make[1]: Entering directory '/home/alignak/alignak'
            dh_installdirs
            make[1]: Leaving directory '/home/alignak/alignak'
               dh_auto_install -O--install-layout=deb,quilt

            # ---
            # Fred: From the get_init_scripts function of install_hooks.cfg
            Installable directories/files: ['']
            Installable directories/files: ['alignak ', '']
            Installable directories/files: ['alignak/log ', '']
            Installable directories/files: ['alignak/run ', '']
            Installable directories/files: ['alignak/libexec ', '']
            Installable directories/files: ['alignak/etc ', ' etc/*']
            Installable directories/files: ['alignak/bin/etc/init.d ', ' systemV/init.d/*']
            Installable directories/files: ['alignak/bin/etc/default ', ' systemV/default/alignak.in']
            Installable directories/files: ['alignak/etc ', ' systemV/alignak.ini']
            # ---

            running install
            running build
            running build_py
            running egg_info
            writing requirements to alignak.egg-info/requires.txt
            writing alignak.egg-info/PKG-INFO
            writing top-level names to alignak.egg-info/top_level.txt
            writing dependency_links to alignak.egg-info/dependency_links.txt
            writing entry points to alignak.egg-info/entry_points.txt
            [pbr] Reusing existing SOURCES.txt
            running install_lib
            creating /home/alignak/alignak/debian/alignak-all/usr/lib
            creating /home/alignak/alignak/debian/alignak-all/usr/lib/python2.7
            creating /home/alignak/alignak/debian/alignak-all/usr/lib/python2.7/dist-packages
            creating /home/alignak/alignak/debian/alignak-all/usr/lib/python2.7/dist-packages/alignak
            copying build/lib.linux-x86_64-2.7/alignak/external_command.py -> /home/alignak/alignak/debian/alignak-all/usr/lib/python2.7/dist-packages/alignak
            copying build/lib.linux-x86_64-2.7/alignak/borg.py -> /home/alignak/alignak/debian/alignak-all/usr/lib/python2.7/dist-packages/alignak
            copying build/lib.linux-x86_64-2.7/alignak/alignakobject.py -> /home/alignak/alignak/debian/alignak-all/usr/lib/python2.7/dist-packages/alignak
            ...
            ...
            ...
            copying build/lib.linux-x86_64-2.7/alignak/bin/alignak_reactionner.py -> /home/alignak/alignak/debian/alignak-all/usr/lib/python2.7/dist-packages/alignak/bin
            copying build/lib.linux-x86_64-2.7/alignak/bin/alignak_receiver.py -> /home/alignak/alignak/debian/alignak-all/usr/lib/python2.7/dist-packages/alignak/bin
            copying build/lib.linux-x86_64-2.7/alignak/bin/alignak_scheduler.py -> /home/alignak/alignak/debian/alignak-all/usr/lib/python2.7/dist-packages/alignak/bin

            running install_data
            creating /home/alignak/alignak/debian/alignak-all/usr/alignak
            creating /home/alignak/alignak/debian/alignak-all/usr/alignak/etc
            creating /home/alignak/alignak/debian/alignak-all/usr/alignak/etc/arbiter
            creating /home/alignak/alignak/debian/alignak-all/usr/alignak/etc/arbiter/daemons
            ...
            ...
            ...
            copying etc/alignak.cfg -> /home/alignak/alignak/debian/alignak-all/usr/alignak/etc/
            copying etc/alignak.ini -> /home/alignak/alignak/debian/alignak-all/usr/alignak/etc/
            ...
            ...
            ...

            running post_hook install_hooks.fix_alignak_cfg for command install_data

            # ---
            # Fred: From the fix_alignak_cfg function of install_hooks.cfg
            ========================================================================================================
            Alignak installation directory: /home/alignak/alignak/debian/alignak-all/usr
            ========================================================================================================


            ========================================================================================================
            Alignak main configuration directories:
             BIN = /home/alignak/alignak/debian/alignak-all/usr/bin
             GROUP = alignak
             LOG = /home/alignak/alignak/debian/alignak-all/usr/alignak/log
             ETC = /home/alignak/alignak/debian/alignak-all/usr/alignak/etc
             USER = alignak
             VAR = /home/alignak/alignak/debian/alignak-all/usr/alignak/libexec
             RUN = /home/alignak/alignak/debian/alignak-all/usr/alignak/run
            ========================================================================================================

            # ---
            # Fred: ok, so the reference for configuration data is in /home/alignak/alignak/debian/alignak-all/usr/alignak/etc
            # ---

            ================================================================================
            ==                                                                            ==
            ==  The installation succeded.                                                ==
            ==                                                                            ==
            == -------------------------------------------------------------------------- ==
            ==                                                                            ==
            == You can run Alignak with:                                                  ==
            ==   /home/alignak/alignak/debian/alignak-all/usr/alignak/bin/etc/init.d/alignak start
            ==                                                                            ==
            == The default installed configuration is located here:                       ==
            ==   /home/alignak/alignak/debian/alignak-all/usr/alignak/etc
            ==                                                                            ==
            == You will find more information about Alignak configuration here:           ==
            ==   http://alignak-doc.readthedocs.io/en/latest/04_configuration/index.html  ==
            ==                                                                            ==
            == -------------------------------------------------------------------------- ==
            ==                                                                            ==
            == You should grant the write permissions on the configuration directory to   ==
            == the user alignak:                                                          ==
            ==   find /home/alignak/alignak/debian/alignak-all/usr/alignak/etc -type f -exec chmod 664 {} +
            ==   find /home/alignak/alignak/debian/alignak-all/usr/alignak/etc -type d -exec chmod 775 {} +
            == -------------------------------------------------------------------------- ==
            ==                                                                            ==
            == You should also grant ownership on those directories to the user alignak:  ==
            ==   chown -R alignak:alignak /home/alignak/alignak/debian/alignak-all/usr/alignak/run
            ==   chown -R alignak:alignak /home/alignak/alignak/debian/alignak-all/usr/alignak/log
            ==   chown -R alignak:alignak /home/alignak/alignak/debian/alignak-all/usr/alignak/libexec
            ==                                                                            ==
            == -------------------------------------------------------------------------- ==
            ==                                                                            ==
            == Please note that installing Alignak with the setup.py script is not the    ==
            == recommended way. You'd rather use the packaging built for your OS          ==
            == distribution that you can find here:                                       ==
            ==   http://alignak-monitoring.github.io/download/                            ==
            ==                                                                            ==
            ================================================================================

            running install_egg_info
            Copying alignak.egg-info to /home/alignak/alignak/debian/alignak-all/usr/lib/python2.7/dist-packages/alignak-0.2.egg-info
            running install_scripts
            Installing alignak-broker script to /home/alignak/alignak/debian/alignak-all/usr/bin
            Installing alignak-scheduler script to /home/alignak/alignak/debian/alignak-all/usr/bin
            Installing alignak-receiver script to /home/alignak/alignak/debian/alignak-all/usr/bin
            Installing alignak-poller script to /home/alignak/alignak/debian/alignak-all/usr/bin
            Installing alignak-reactionner script to /home/alignak/alignak/debian/alignak-all/usr/bin
            Installing alignak-arbiter script to /home/alignak/alignak/debian/alignak-all/usr/bin
               debian/rules override_dh_install
            make[1]: Entering directory '/home/alignak/alignak'
            dh_install
            #mv /home/alignak/alignak/debian/alignak-all/usr/etc/default /home/alignak/alignak/debian/alignak-all/etc/
            rm -rf /home/alignak/alignak/debian/alignak-all/usr/etc/
            rm -rf /home/alignak/alignak/debian/alignak-all/usr/var/
            make[1]: Leaving directory '/home/alignak/alignak'
               dh_installdocs -O--install-layout=deb,quilt
               dh_installchangelogs -O--install-layout=deb,quilt
               dh_installman -O--install-layout=deb,quilt
               dh_python2 -O--install-layout=deb,quilt
            W: dh_python2:479: Please add dh-python package to Build-Depends
               debian/rules override_dh_installinit
            make[1]: Entering directory '/home/alignak/alignak'
            dh_installinit --no-start --name=alignak
            make[1]: Leaving directory '/home/alignak/alignak'
               dh_perl -O--install-layout=deb,quilt
               dh_link -O--install-layout=deb,quilt
               dh_compress -O--install-layout=deb,quilt
               dh_fixperms -O--install-layout=deb,quilt
               dh_installdeb -O--install-layout=deb,quilt
               dh_gencontrol -O--install-layout=deb,quilt
            dpkg-gencontrol: warning: package alignak-all: unused substitution variable ${python:Versions}
               dh_md5sums -O--install-layout=deb,quilt
               dh_builddeb -O--install-layout=deb,quilt
            dpkg-deb: building package `alignak-all' in `../alignak-all_0.2-1_all.deb'.
             dpkg-genchanges  >../alignak_0.2-1_amd64.changes
            dpkg-genchanges: including full source code in upload
             dpkg-source --after-build alignak
            dpkg-buildpackage: full upload (original source is included)

    # Check package compliance
    lintian ../alignak*.deb
            W: alignak-all: non-standard-dir-in-usr usr/alignak/
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/alignak.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/alignak.ini
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/daemons/arbiter-master.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/daemons/broker-master.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/daemons/poller-master.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/daemons/reactionner-master.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/daemons/receiver-master.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/daemons/scheduler-master.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/modules/readme.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/objects/commands/detailled-host-by-email.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/objects/commands/detailled-service-by-email.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/objects/commands/notify-host-by-email.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/objects/commands/notify-service-by-email.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/objects/contactgroups/admins.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/objects/contactgroups/users.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/objects/contacts/admin.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/objects/contacts/guest.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/objects/dependencies/sample.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/objects/escalations/sample.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/objects/hostgroups/linux.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/objects/hosts/localhost.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/objects/notificationways/detailled-email.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/objects/notificationways/email.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/objects/realms/all.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/objects/servicegroups/sample.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/objects/services/services.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/objects/timeperiods/24x7.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/objects/timeperiods/none.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/objects/timeperiods/us-holidays.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/objects/timeperiods/workhours.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/packs/readme.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/packs/resource.d/readme.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/resource.d/paths.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/templates/business-impacts.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/templates/generic-contact.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/templates/generic-host.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/templates/generic-service.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/arbiter/templates/time_templates.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/certs/README
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/daemons/arbiterd.ini
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/daemons/brokerd.ini
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/daemons/pollerd.ini
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/daemons/reactionnerd.ini
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/daemons/receiverd.ini
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/daemons/schedulerd.ini
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hostgroups.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hosts/br-erp.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hosts/srv-collectd.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hosts/srv-emc-clariion.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hosts/srv-esx.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hosts/srv-exchange-cas.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hosts/srv-exchange-ht.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hosts/srv-exchange-mb.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hosts/srv-exchange-um.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hosts/srv-iis.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hosts/srv-linux.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hosts/srv-microsoft-dc.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hosts/srv-mongodb.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hosts/srv-mysql.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hosts/srv-netapp.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hosts/srv-newyork.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hosts/srv-oracle.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hosts/srv-postgresql.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hosts/srv-vmware-vm.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hosts/srv-web-avg.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hosts/srv-webserver.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hosts/srv-windows.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/hosts/switch-cisco.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/services/eue_glpi.cfg
            W: alignak-all: file-in-unusual-dir usr/alignak/etc/sample/sample/triggers.d/avg_http.trig
            W: alignak-all: init.d-script-not-marked-as-conffile etc/init.d/alignak-scheduler
            E: alignak-all: init.d-script-not-included-in-package etc/init.d/alignak-scheduler
            W: alignak-all: init.d-script-not-marked-as-conffile etc/init.d/alignak-broker
            E: alignak-all: init.d-script-not-included-in-package etc/init.d/alignak-broker
            W: alignak-all: init.d-script-not-marked-as-conffile etc/init.d/alignak-receiver
            E: alignak-all: init.d-script-not-included-in-package etc/init.d/alignak-receiver
            W: alignak-all: init.d-script-not-marked-as-conffile etc/init.d/alignak-arbiter
            E: alignak-all: init.d-script-not-included-in-package etc/init.d/alignak-arbiter
            W: alignak-all: init.d-script-not-marked-as-conffile etc/init.d/alignak-poller
            E: alignak-all: init.d-script-not-included-in-package etc/init.d/alignak-poller
            W: alignak-all: init.d-script-not-marked-as-conffile etc/init.d/alignak-reactionner
            E: alignak-all: init.d-script-not-included-in-package etc/init.d/alignak-reactionner
            W: alignak-all: init.d-script-not-marked-as-conffile etc/init.d/alignak
            E: alignak-all: init.d-script-not-included-in-package etc/init.d/alignak
            W: alignak-all: executable-not-elf-or-script etc/alignak/daemons/receiverd.ini
            W: alignak-all: executable-not-elf-or-script usr/alignak/etc/daemons/schedulerd.ini
            W: alignak-all: executable-not-elf-or-script etc/alignak/daemons/brokerd.ini
            W: alignak-all: executable-not-elf-or-script etc/alignak/alignak.cfg
            W: alignak-all: executable-not-elf-or-script usr/alignak/etc/daemons/brokerd.ini
            W: alignak-all: executable-not-elf-or-script etc/alignak/daemons/arbiterd.ini
            W: alignak-all: executable-not-elf-or-script etc/alignak/alignak.ini
            W: alignak-all: executable-not-elf-or-script etc/alignak/daemons/schedulerd.ini
            W: alignak-all: executable-not-elf-or-script usr/alignak/etc/daemons/reactionnerd.ini
            W: alignak-all: executable-not-elf-or-script usr/alignak/etc/daemons/pollerd.ini
            W: alignak-all: executable-not-elf-or-script etc/alignak/daemons/reactionnerd.ini
            W: alignak-all: executable-not-elf-or-script usr/alignak/etc/daemons/arbiterd.ini
            W: alignak-all: executable-not-elf-or-script usr/alignak/etc/daemons/receiverd.ini
            W: alignak-all: executable-not-elf-or-script usr/alignak/etc/alignak.cfg
            W: alignak-all: executable-not-elf-or-script lib/systemd/system/alignak.ini
            W: alignak-all: executable-not-elf-or-script etc/alignak/daemons/pollerd.ini
            W: alignak-all: executable-not-elf-or-script usr/alignak/etc/alignak.ini
            W: alignak-all: maintainer-script-ignores-errors postinst
            W: alignak-all: systemd-service-file-refers-to-obsolete-target lib/systemd/system/alignak-arbiter.service syslog.target
            W: alignak-all: systemd-service-file-refers-to-obsolete-target lib/systemd/system/alignak-broker.service syslog.target
            W: alignak-all: systemd-service-file-refers-to-obsolete-target lib/systemd/system/alignak-poller.service syslog.target
            W: alignak-all: systemd-service-file-refers-to-obsolete-target lib/systemd/system/alignak-reactionner.service syslog.target
            W: alignak-all: systemd-service-file-refers-to-obsolete-target lib/systemd/system/alignak-receiver.service syslog.target
            W: alignak-all: systemd-service-file-refers-to-obsolete-target lib/systemd/system/alignak-scheduler.service syslog.target
            W: alignak-all: maintainer-script-calls-systemctl prerm:28
            W: alignak-all: maintainer-script-calls-systemctl postrm:41
            W: alignak-all: maintainer-script-calls-systemctl postrm:42
            W: alignak-all: maintainer-script-calls-systemctl postrm:43
            W: alignak-all: maintainer-script-calls-systemctl postrm:44
            W: alignak-all: maintainer-script-calls-systemctl postrm:45
            W: alignak-all: maintainer-script-calls-systemctl postrm:46
            W: alignak-all: maintainer-script-calls-systemctl postinst:59
            W: alignak-all: maintainer-script-calls-systemctl postinst:60
            W: alignak-all: maintainer-script-calls-systemctl postinst:61
            W: alignak-all: maintainer-script-calls-systemctl postinst:62
            W: alignak-all: maintainer-script-calls-systemctl postinst:63
            W: alignak-all: maintainer-script-calls-systemctl postinst:64


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



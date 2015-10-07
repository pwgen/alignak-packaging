%global alignak_user nagios
%global alignak_group nagios

Summary:        Python Monitoring tool
Name:           alignak
Version:        0.0.4
Release:        1%{?dist}
URL:            https://github.com/Alignak-monitoring/%{name}
Source0:        https://github.com/Alignak-monitoring/%{name}/archive/%{version}.tar.gz 
Source1:        %{name}-arbiter.service 
Source2:       	%{name}-broker.service 
Source3:       	%{name}-reactionner.service 
Source4:       	%{name}-receiver.service 
Source5:       	%{name}-poller.service 
Source6:       	%{name}-scheduler.service 
Source7:       	%{name}.logrotate
Source8:        %{name}-tmpfiles.conf 
License:        AGPLv3+
Requires:       python-simplejson 
Requires:       python-pycurl  
Requires:       python-cherrypy 
Requires:       python-requests
Requires:       python-setproctitle
Requires:       python-ujson
Requires:       python-termcolor
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr
BuildRequires:  systemd-units

BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot
Buildarch:      noarch

%description 
Alignak is a new monitoring tool written in Python. 
The main goal of Alignak is to allow users to have a fully flexible 
architecture for their monitoring system that can easily scale to large 
environments.

%package all
Summary: Meta-package to pull in all alignak 
Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-arbiter = %{version}-%{release}
Requires: %{name}-broker = %{version}-%{release}
Requires: %{name}-scheduler = %{version}-%{release}
Requires: %{name}-reactionner = %{version}-%{release}
Requires: %{name}-receiver = %{version}-%{release}
Requires: %{name}-poller = %{version}-%{release}

%description all
Alignak is a new monitoring tool written in Python. 
The main goal of Alignak is to allow users to have a fully flexible 
architecture for their monitoring system that can easily scale to large 
environments.

This is a dummy package which brings in all subpackages.

%package common
Summary: Alignak Common 

%description common
Alignak Common

%package arbiter
Summary: Alignak Arbiter 
Requires: %{name}-common = %{version}-%{release}

%description arbiter
Alignak arbiter daemon

%package reactionner
Summary: Alignak Reactionner
Requires: %{name}-common = %{version}-%{release}

%description reactionner
Alignak reactionner daemon

%package scheduler
Summary: Alignak Scheduler
Requires: %{name}-common = %{version}-%{release}

%description scheduler
Alignak scheduler daemon

%package poller
Summary: Alignak Poller
Requires: %{name}-common = %{version}-%{release}
Requires: nagios-plugins-all

%description poller
Alignak poller daemon

%package broker
Summary: Alignak Broker
Requires: %{name}-common = %{version}-%{release}

%description broker
Alignak broker daemon

%package receiver
Summary: Alignak Poller
Requires: %{name}-common = %{version}-%{release}

%description receiver
Alignak receiver daemon

%prep

%setup -q -n %{name}-%{version}

# clean git files/
find . -name '.gitignore' -exec rm -f {} \;
find . -name '.gitempty' -exec rm -f {} \;
find . -name '.gitkeep' -exec rm -f {} \;

%build

%py2_build

%install

find %{buildroot} -size 0 -delete

%py2_install

install -d -m0755 %{buildroot}%{_unitdir}
install -p -m0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}-arbiter.service
install -p -m0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}-broker.service
install -p -m0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}-reactionner.service
install -p -m0644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}-receiver.service
install -p -m0644 %{SOURCE5} %{buildroot}%{_unitdir}/%{name}-poller.service
install -p -m0644 %{SOURCE6} %{buildroot}%{_unitdir}/%{name}-scheduler.service

install -d -m0755  %{buildroot}%{_sysconfdir}/%{name}/
rm -rf %{buildroot}%{_sysconfdir}/%{name}/*

rm -rf %{buildroot}/usr/etc/%{name}/*
rm -rf %{buildroot}/usr/etc/default/%{name}

rm %{buildroot}/%{python_sitelib}/*pth

cp -r %{_builddir}/%{name}/etc/* %{buildroot}%{_sysconfdir}/%{name}
rm -rf %{buildroot}%{_sysconfdir}/%{name}/sample
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}/modules

install -d -m0755 %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m0644 %{SOURCE7} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

install -d -m0755 %{buildroot}%{_sysconfdir}/tmpfiles.d
install -m0644  %{SOURCE8} %{buildroot}%{_sysconfdir}/tmpfiles.d/%{name}.conf

install -d -m0755 %{buildroot}%{_localstatedir}/log/%{name}
install -d -m0755 %{buildroot}%{_localstatedir}/log/%{name}/archives
install -d -m0755 %{buildroot}%{_localstatedir}/lib/%{name}

mkdir -p %{buildroot}%{_localstatedir}/run/
install -d -m0755 %{buildroot}%{_localstatedir}/run/%{name}

rm -rf %{buildroot}/usr/etc/init.d/*

%clean

%pre 
getent group %{alignak_group} >/dev/null || groupadd -r %{alignak_group}
getent passwd %{alignak_user} >/dev/null || useradd -r -g %{alignak_group} -d %{_localstatedir}/spool/nagios -s /sbin/nologin %{alignak_user}
exit 0

%post arbiter
if [ $1 -eq 1 ] ; then 
  /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post broker
if [ $1 -eq 1 ] ; then 
  /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post poller
if [ $1 -eq 1 ] ; then 
  /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post reactionner
if [ $1 -eq 1 ] ; then 
  /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post scheduler
if [ $1 -eq 1 ] ; then 
  /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post receiver
if [ $1 -eq 1 ] ; then 
  /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun arbiter 
if [ $1 -eq 0 ] ; then
  /bin/systemctl --no-reload disable %{name}-arbiter.service > /dev/null 2>&1 || :
  /bin/systemctl stop %{name}-arbiter.service > /dev/null 2>&1 || :
fi

%preun broker 
if [ $1 -eq 0 ] ; then
  /bin/systemctl --no-reload disable %{name}-broker.service > /dev/null 2>&1 || :
  /bin/systemctl stop %{name}-broker.service > /dev/null 2>&1 || :
fi

%preun poller 
if [ $1 -eq 0 ] ; then
  /bin/systemctl --no-reload disable %{name}-poller.service > /dev/null 2>&1 || :
  /bin/systemctl stop %{name}-poller.service > /dev/null 2>&1 || :
fi

%preun reactionner 
if [ $1 -eq 0 ] ; then
  /bin/systemctl --no-reload disable %{name}-reactionner.service > /dev/null 2>&1 || :
  /bin/systemctl stop %{name}-reactionner.service > /dev/null 2>&1 || :
fi

%preun scheduler 
if [ $1 -eq 0 ] ; then
  /bin/systemctl --no-reload disable %{name}-scheduler.service > /dev/null 2>&1 || :
  /bin/systemctl stop %{name}-scheduler.service > /dev/null 2>&1 || :
fi

%preun receiver 
if [ $1 -eq 0 ] ; then
  /bin/systemctl --no-reload disable %{name}-receiver.service > /dev/null 2>&1 || :
  /bin/systemctl stop %{name}-receiver.service > /dev/null 2>&1 || :
fi

%postun arbiter
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
  /bin/systemctl try-restart %{name}-arbiter.service >/dev/null 2>&1 || :
fi

%postun broker
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
  /bin/systemctl try-restart %{name}-broker.service >/dev/null 2>&1 || :
fi

%postun poller
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
  /bin/systemctl try-restart %{name}-poller.service >/dev/null 2>&1 || :
fi

%postun reactionner
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
  /bin/systemctl try-restart %{name}-reactionner.service >/dev/null 2>&1 || :
fi

%postun scheduler
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
  /bin/systemctl try-restart %{name}-scheduler.service >/dev/null 2>&1 || :
fi

%postun receiver
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
  /bin/systemctl try-restart %{name}-receiver.service >/dev/null 2>&1 || :
fi

%files arbiter
%{_unitdir}/%{name}-arbiter.service
%{_bindir}/%{name}-arbiter*
%config(noreplace) %{_sysconfdir}/%{name}
#%config(noreplace) %{_sysconfdir}/%{name}/%{name}.cfg
#%config(noreplace) %{_sysconfdir}/%{name}/arbiters/arbiter-master.cfg
#%config(noreplace) %{_sysconfdir}/%{name}/brokers/broker-master.cfg
#%config(noreplace) %{_sysconfdir}/%{name}/pollers/poller-master.cfg
#%config(noreplace) %{_sysconfdir}/%{name}/reactionners/reactionner-master.cfg
#%config(noreplace) %{_sysconfdir}/%{name}/receivers/receiver-master.cfg
#%config(noreplace) %{_sysconfdir}/%{name}/schedulers/scheduler-master.cfg
#%config(noreplace) %{_sysconfdir}/%{name}/commands/commands.cfg
#%config(noreplace) %{_sysconfdir}/%{name}/timeperiods/timeperiods.cfg
#%config %{_sysconfdir}/%{name}/escalations
#%config %{_sysconfdir}/%{name}/dependencies
#%config(noreplace) %{_sysconfdir}/%{name}/templates/templates.cfg
#%config %{_sysconfdir}/%{name}/notificationways
#%config %{_sysconfdir}/%{name}/servicegroups
#%config %{_sysconfdir}/%{name}/hostgroups
#%config(noreplace) %{_sysconfdir}/%{name}/contactgroups/contactgroups.cfg
#%config(noreplace) %{_sysconfdir}/%{name}/hosts/localhost.cfg
#%config(noreplace) %{_sysconfdir}/%{name}/services/linux_disks.cfg
#%config(noreplace) %{_sysconfdir}/%{name}/contacts/nagiosadmin.cfg
#%config %{_sysconfdir}/%{name}/packs
#%config %{_sysconfdir}/%{name}/modules
#%config(noreplace) %{_sysconfdir}/%{name}/realms/all.cfg
#%config %{_sysconfdir}/%{name}/resource.d

#%{_mandir}/man8/%{name}-arbiter*

%files reactionner
%{_unitdir}/%{name}-reactionner.service
%{_bindir}/%{name}-reactionner*
#%{_mandir}/man8/%{name}-reactionner*
#%config(noreplace) %{_sysconfdir}/%{name}/daemons/reactionnerd.ini

%files scheduler
%{_unitdir}/%{name}-scheduler.service
%{_bindir}/%{name}-scheduler*
#%{_mandir}/man8/%{name}-scheduler*
#%config(noreplace) %{_sysconfdir}/%{name}/daemons/schedulerd.ini

%files poller
%{_unitdir}/%{name}-poller.service
%{_bindir}/%{name}-poller*
#%{_mandir}/man8/%{name}-poller*
#%config(noreplace) %{_sysconfdir}/%{name}/daemons/pollerd.ini

%files broker
%{_unitdir}/%{name}-broker.service
%{_bindir}/%{name}-broker*
#%{_mandir}/man8/%{name}-broker*
#%config(noreplace) %{_sysconfdir}/%{name}/daemons/brokerd.ini

%files receiver
%{_unitdir}/%{name}-receiver.service
%{_bindir}/%{name}-receiver*
#%{_mandir}/man8/%{name}-receiver*
#%config(noreplace) %{_sysconfdir}/%{name}/daemons/receiverd.ini

%files common
%{python_sitelib}/%{name}
%{python_sitelib}/alignak*.egg-info
%doc COPYING THANKS 
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/tmpfiles.d/%{name}.conf
%attr(-,%{alignak_user} ,%{alignak_group}) %dir %{_localstatedir}/log/%{name}
%attr(-,%{alignak_user} ,%{alignak_group}) %{_localstatedir}/lib/%{name}
%attr(-,%{alignak_user} ,%{alignak_group}) %dir %{_localstatedir}/run/%{name}

%files all
# No files for you!

%changelog
* Sun Aug 23 2015 David Hannequin <david.hannequin@gmail.com> - 0.0.4-1
- Fisrt release for Fedora.

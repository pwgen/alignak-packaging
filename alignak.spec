%global alignak_user alignak
%global alignak_group alignak

Summary:        Python Monitoring tool
Name:           alignak
Version:        0.0.1
Release:        5
URL:            https://github.com/Alignak-monitoring/alignak 
Source0:        %{name}-%{version}.tar.gz
License:        AGPLv3+

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr
BuildRequires:  make

Group:          Application/System

#BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot
#BuildArch:      noarch

%description
Alignak is a new monitoring tool written in Python.
The main goal of Alignak is to allow users to have a fully flexible
architecture for their monitoring system that can easily scale to large
environments.
Alignak also provide interfaces with NDODB and Merlin database,
Livestatus connector Alignak does not include any human interfaces.

%package common
Summary: Alignak Common files
Group:          Application/System
Requires:       python

%description common
Common files for alignak monitoring



%prep
%setup -qn %{name}
#%setup -qn alignak

# Apply all patches
# TODO check patch from shinken packaging
#for patch_file in $(cat debian/patches/series | grep -v "^#")
#do
#%{__patch} -p1 < debian/patches/$patch_file
#done


%build
%{__python} setup.py build

%install

#find %{buildroot} -size 0 -delete
#rm -rf %_buildrootdir %{buildroot}/*
#rm -rf %{buildroot}/*#

%{__python} setup.py install -O1 --root=%{buildroot} --install-scripts=%{_sbindir} --install-lib=%{python_sitelib}
#%{__python} setup.py install -O1 --root=%_buildrootdir --install-scripts=%{_sbindir} --install-lib=%{python_sitelib}


install -d -m0755  %{buildroot}%{_sysconfdir}/%{name}/
rm -rf %{buildroot}%{_sysconfdir}/%{name}/*
rm -rf %{buildroot}/usr/etc/%{name}/*
rm -rf %{buildroot}/usr/etc/default/%{name}
install -d -m0755 %{buildroot}/usr/share/pyshared/alignak


# Clean useless
rm -rf %{buildroot}/var/lib/alignak/share/templates
rm -rf %{buildroot}/var/lib/alignak/share/images
rm -rf %{buildroot}/%{python_sitelib}/modules/
rm -rf %{buildroot}/var/lib/alignak/doc/
rm -rf %{buildroot}/etc/alignak/packs/.placeholder
rm -rf %{buildroot}/var/lib/alignak/inventory/
rm -rf %{buildroot}/var/lib/alignak/libexec/
rm -rf %{buildroot}/var/lib/alignak/libexec/
rm -rf %{buildroot}/etc/init.d

# log
install -d -m0755 %{buildroot}%{_localstatedir}/log/%{name}
install -d -m0755 %{buildroot}%{_localstatedir}/log/%{name}/archives
# run
mkdir -p %{buildroot}%{_localstatedir}/run/
install -d -m0755 %{buildroot}%{_localstatedir}/run/%{name}
# etc

ls %{_builddir}/%{name}/etc
ls %{buildroot}%{_sysconfdir}

cp -r %{_builddir}/%{name}/etc/* %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/modules





%clean
rm -rf %{buildroot}

%files
#/%{_unitdir}
%{python_sitelib}/%{name}
%{python_sitelib}/alignak-*.egg-info
/usr/share/pyshared/alignak
%attr(-,%{alignak_user} ,%{alignak_group}) %dir %{_localstatedir}/log/%{name}
%attr(-,%{alignak_user} ,%{alignak_group}) %dir %{_localstatedir}/run/%{name}
# arbiter
/%{_sbindir}/%{name}-arbiter
%config(noreplace) %{_sysconfdir}/%{name}/alignak.cfg
%config(noreplace) %{_sysconfdir}/%{name}/certs/
%config(noreplace) %{_sysconfdir}/%{name}/hosts/
%config(noreplace) %{_sysconfdir}/%{name}/packs/
%config(noreplace) %{_sysconfdir}/%{name}/modules/
%config(noreplace) %{_sysconfdir}/%{name}/commands/
%config(noreplace) %{_sysconfdir}/%{name}/contacts/
%config(noreplace) %{_sysconfdir}/%{name}/contactgroups/
%config(noreplace) %{_sysconfdir}/%{name}/resource.d/
%config(noreplace) %{_sysconfdir}/%{name}/templates/
%config(noreplace) %{_sysconfdir}/%{name}/timeperiods/
%config(noreplace) %{_sysconfdir}/%{name}/arbiters/arbiter-master.cfg
%config(noreplace) %{_sysconfdir}/%{name}/realms/
%config(noreplace) %{_sysconfdir}/%{name}/notificationways/
# TODO: remove: Seems Useless
%config(noreplace) %{_sysconfdir}/%{name}/hostgroups/
%config(noreplace) %{_sysconfdir}/%{name}/services/
%config(noreplace) %{_sysconfdir}/%{name}/servicegroups/
%config(noreplace) %{_sysconfdir}/%{name}/dependencies/
%config(noreplace) %{_sysconfdir}/%{name}/escalations/
#reactionner
/%{_sbindir}/%{name}-reactionner
%config(noreplace) %{_sysconfdir}/%{name}/daemons/reactionnerd.ini
%config(noreplace) %{_sysconfdir}/%{name}/reactionners/reactionner-master.cfg
%config(noreplace) %{_sysconfdir}/%{name}/reactionners/reactionner-android-sms.cfg
# scheduler
/%{_sbindir}/%{name}-scheduler
%config(noreplace) %{_sysconfdir}/%{name}/daemons/schedulerd.ini
%config(noreplace) %{_sysconfdir}/%{name}/schedulers/scheduler-master.cfg
# poller
/%{_sbindir}/%{name}-poller
#%config(noreplace) %{_sysconfdir}/%{name}/daemons/pollerd.ini
%config(noreplace) %{_sysconfdir}/%{name}/pollers/poller-master.cfg
# broker
/%{_sbindir}/%{name}-broker
%config(noreplace) %{_sysconfdir}/%{name}/daemons/brokerd.ini
%config(noreplace) %{_sysconfdir}/%{name}/brokers/broker-master.cfg
# receiver
/%{_sbindir}/%{name}-receiver
%config(noreplace) %{_sysconfdir}/%{name}/daemons/receiverd.ini
%config(noreplace) %{_sysconfdir}/%{name}/receivers/receiver-master.cfg

%changelog
* Thu Jun 11 2015 Thibault Cohen <thibault.cohen@savoirfairelinux.com> - 0.0.1-20150611
- Initial package

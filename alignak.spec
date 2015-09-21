%global alignak_user alignak
%global alignak_group alignak

Summary:        Python Monitoring tool
Name:           alignak
Version:        0.1
Release:        1
URL:            https://github.com/Alignak-monitoring/alignak 
Source0:        %{name}-%{version}.tar.gz
License:        AGPLv3+

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr

Group:          Application/System


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
Requires:       python >= 2.6
Requires:       python-cherrypy
Requires:       python-requests >= 2.6.0
Requires:       python-termcolor
Requires:       python-setproctitle
#Requires:       python-ujson


%description common
Common files for alignak monitoring



%prep
%setup -qn %{name}

# Apply all patches
# TODO check patch from shinken packaging
#for patch_file in $(cat debian/patches/series | grep -v "^#")
#do
#%{__patch} -p1 < debian/patches/$patch_file
#done


%build
%{py_build}

%install

# See if we want usr/bin or usr/sbin for bin : --install-scripts=%{_sbindir}
%{__python} setup.py install -O1 --root=%{buildroot} --install-lib=%{python_sitelib}

install -d -m0755  %{buildroot}%{_sysconfdir}/%{name}/
rm -rf %{buildroot}%{_sysconfdir}/%{name}/*

# Remove generated conf
rm -rf %{buildroot}/usr/etc/%{name}/*
rm -rf %{buildroot}/usr/etc/default/%{name}

#Remove .pth
rm %{buildroot}/%{python_sitelib}/*pth

# Copy original file but remove sample
cp -r %{_builddir}/%{name}/etc/* %{buildroot}%{_sysconfdir}/%{name}
rm -rf %{buildroot}%{_sysconfdir}/%{name}/sample
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}/modules

# init script, remove it with systemd
install -d -m0755 %{buildroot}%{_sysconfdir}/init.d/
mv %{buildroot}/usr/etc/init.d/* %{buildroot}%{_sysconfdir}/init.d/
install -d -m0755 %{buildroot}%{_sysconfdir}/default

sed -i -e 's:\$ETC\$:%{_sysconfdir}/%{name}:g' \
    -e 's:\$VAR\$:%{_localstatedir}:g' \
    -e 's:\$RUN\$:%{_localstatedir}/run:g' \
    -e 's:\$SCRIPTS_BIN\$:%{_bindir}:g' \
    -e 's:\$LOG\$:%{_localstatedir}/log:g' \
    %{_builddir}/%{name}/bin/default/%{name}.in

cp %{_builddir}/%{name}/bin/default/%{name}.in %{buildroot}%{_sysconfdir}/default/%{name}


# log
install -d -m0755 %{buildroot}%{_localstatedir}/log/%{name}
install -d -m0755 %{buildroot}%{_localstatedir}/log/%{name}/archives

# run
mkdir -p %{buildroot}%{_localstatedir}/run/
install -d -m0755 %{buildroot}%{_localstatedir}/run/%{name}

# Module, for new style module setup (namespace will do the job)
install -d -m0755 %{buildroot}/usr/share/pyshared/%{name}

%clean
rm -rf %{buildroot}

%files common
# Alignak python lib
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}*.egg-info

# Module, for new style module setup (namespace will do the job)
/usr/share/pyshared/%{name}

# Log and run dir 
%attr(-,%{alignak_user} ,%{alignak_group}) %dir %{_localstatedir}/log/%{name}
%attr(-,%{alignak_user} ,%{alignak_group}) %dir %{_localstatedir}/run/%{name}

# Basic config
%config(noreplace) %{_sysconfdir}/%{name}/*

# Daemon python binaries
/%{_bindir}/%{name}-*

# Init script. Maybe we should exclude this when systemd in setup
%{_sysconfdir}/init.d/%{name}*
%{_sysconfdir}/default/%{name}

%changelog
* Sun Sep 20 2015 Sebastien Coavoux <alignak@pyseb.cx> - 0.1-1
- Initial package

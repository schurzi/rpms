# Authority: dag

# Upstream: <kingleo@gmx.at>

%define plugindir %(xmms-config --general-plugin-dir)

%define rname real_random

Summary: A plugin for XMMS providing better shuffling.
Name: xmms-real-random
Version: 0.3
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://home.pages.at/kingleo/index.php?show=/development/stuff

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://home.pages.at/kingleo/development/stuff/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: xmms-devel

%description
A plugin for XMMS providing better shuffling.

%prep
%setup -n %{rname}-%{version}

%build
%configure \
        --enable-shared \
        --libdir="%{plugindir}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	libdir="%{buildroot}%{plugindir}"

### Clean up buildroot
%{__rm} -f %{buildroot}%{plugindir}/*.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{plugindir}/*.so
#exclude %{plugindir}/*.la

%changelog
* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 0.3-0
- Updated to release 0.3.

* Mon Apr 07 2003 Dag Wieers <dag@wieers.com> - 0.2-0
- Initial package. (using DAR)

# Authority: dag

%define _libdir %{_prefix}/lib/remedial/

Summary: Remedial AVI player.
Name: remedial
Version: 0.2.22
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://leapster.org/remedial/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://apt.leapster.org/src/remedial/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: avifile-devel >= 0.7.7, expat-devel
BuildRequires: qt-devel >= 2.1.0, libvorbis-devel, libao-devel, libmad-devel

%description
Remedial is a front-end for the avifile libraries.

%prep
%setup

%build
%{?rhfc1:export QTDIR="/usr/lib/qt-3.1"}
%{?rhel3:export QTDIR="/usr/lib/qt-3.1"}
%{?rh90:export QTDIR="/usr/lib/qt3"}
%{?rh80:export QTDIR="/usr/lib/qt3"}
%{?rh73:export QTDIR="/usr/lib/qt2"}
%{?rhel21:export QTDIR="/usr/lib/qt2"}
%{?rh62:export QTDIR="/usr/lib/qt-2.1.0"}
CFLAGS="%{optflags}" ./am_edit --no-final
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/remedial/*.la

%post
/sbin/ldconfig 2>/dev/null

%postun 
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING LICENCE NEWS README
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/remedial.xml
%{_bindir}/*
%{_libdir}/

%changelog
* Sat Dec 20 2003 Dag Wieers <dag@wieers.com> - 0.2.22-0
- Initial package. (using DAR)

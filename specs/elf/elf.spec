# Authority: dag

%define rversion 0.5.4p1

Summary: A simple ELF header analyzer.
Name: elf
Version: 0.5.4
Release: 0.p1
License: GPL
Group: Applications/System
URL: http://www.kerneled.com/projects/elf/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.kerneled.com/projects/elf/%{name}-%{rversion}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

#BuildRequires: 

%description
elf is an ELF header (e_header) analysis tool. It allows you to gather
various information from a binary's ELF header. An intuitive interactive
and command-line mode is available. 

%prep
%setup -n %{name}-%{rversion}

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e '
		s|\$\(BINDIR\)|\$(bindir)|;
		s|\$\(INSDIR\)|\$(mandir)/man1|;
	' src/Makefile.in doc/Makefile.in

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
### FIXME: Makefile doesn't create target directories (Please fix upstream)
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1/
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING CREDITS README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sun Oct 19 2003 Dag Wieers <dag@wieers.com> - 0.5.4-0.p1
- Updated to release 0.5.4p1.

* Fri Sep 19 2003 Dag Wieers <dag@wieers.com> - 0.5.4-0
- Initial package. (using DAR)

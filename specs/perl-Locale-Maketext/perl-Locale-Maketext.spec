# Authority: dag

# Dists: rh73

%define rname Locale-Maketext

Summary: A framework for localization and inheritance-based lexicons for Perl.
Name: perl-Locale-Maketext
Version: 1.06
Release: 0
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Locale-Maketext/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/S/SB/SBURKE/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Locale::Maketext is a base class providing a framework for
localization and inheritance-based lexicons, as described in my
article in The Perl Journal #13 (a corrected version of which appears
in this dist).

%prep
%setup -n %{rname}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/

%changelog
* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 1.06-0
- Updated to release 1.06.

* Sat Feb 01 2003 Dag Wieers <dag@wieers.com> - 1.03-0
- Initial package. (using DAR)

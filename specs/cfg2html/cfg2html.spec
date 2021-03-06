# $Id$
# Authority: dag
# Upstream: 

%define real_name cfg2html-linux


Summary: Tool to collect Linux system configuration into a HTML and text file.
Name: cfg2html
Version: 1.79
%define real_version %{version}-20101104
Release: 1%{?dist}
License: Unknown
Group: Applications/System
URL: http://www.cfg2html.com/

Source: http://www.cfg2html.com/cfg2html-linux-%{real_version}_all.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch

Provides: cfg2html-linux = %{version}-%{release}
Obsoletes: cfg2html-linux <= %{version}-%{release}

%description
Config to HTML is the "swiss army knife" for the ASE, CE, sysadmin etc. It helps
to get the nessary informations to plan an update, to performe basic trouble
shooting or performance analysis.

As a bonus cfg2html creates a nice HTML and plain ASCII documentation from
Linux System, Cron and At, installed Hardware, installed Software,
Filesystems, Dump- and Swapconfiguration, LVM, Network Settings,
Kernel, Systemenhancements and Applications, Subsystems.

%prep
%setup -c

%{__mv} %{name}-linux_%{version}-1_i386.changes Changes
%{__mv} descript.ion README

tar -xvzf %{name}-linux_%{version}-1.tar.gz
cd %{name}-linux-%{version}

%build

%install
%{__rm} -rf %{buildroot}
cd %{name}-linux-%{version}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man8/
%{__make} install DESTDIR="%{buildroot}"

%{__ln_s} -f cfg2html-linux.8 %{buildroot}%{_mandir}/man8/cfg2html.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README*
%doc %{name}-linux-%{version}/AUTHORS
%doc %{name}-linux-%{version}/contrib/
%doc %{name}-linux-%{version}/collect/
%doc %{name}-linux-%{version}/README
%doc %{name}-linux-%{version}/*.html
%doc %{name}-linux-%{version}/*.txt
%doc %{_mandir}/man8/cfg2html.8*
%doc %{_mandir}/man8/cfg2html-linux.8*
%config %{_sysconfdir}/cfg2html/
%{_bindir}/cfg2html
%{_bindir}/cfg2html-linux

%changelog
* Wed Nov 17 2010 Dag Wieers <dag@wieers.com> - 1.79-1
- Updated to release 1.79.
- Fix wrong conflict.

* Mon Jun 07 2010 Dag Wieers <dag@wieers.com> - 1.78-1
- Initial package. (using DAR)

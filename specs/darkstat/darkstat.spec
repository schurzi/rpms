# $Id: _template.spec 130 2004-03-17 10:51:35Z dude $

# Authority: dag
# Upstream: Emil Mikulic <www-28ab@dmr.ath.cx>

Summary: Network traffic analyzer.
Name: darkstat
Version: 2.6
Release: 1
License: GPL
Group: Applications/Internet
URL: http://dmr.ath.cx/net/darkstat/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dmr.ath.cx/net/darkstat/darkstat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap

%description
darkstat is a network traffic analyzer. It's basically a packet sniffer
which runs as a background process on a cable/DSL router and gathers
all sorts of useless but interesting statistics.

%prep
%setup

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL ISSUES NEWS README
%doc %{_mandir}/man?/*
%{_sbindir}/*

%changelog
* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 2.6-1
- Initial package. (using DAR)

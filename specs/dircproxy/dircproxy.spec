# Authority: dag

Summary: IRC proxy server.
Name: dircproxy
Version: 1.0.5
Release: 0
License: GPL
Group: Applications/Internet
URL: http://www.dircproxy.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.dircproxy.net/pub/dircproxy/1.0/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
dircproxy is an IRC proxy server designed for people who use IRC from
lots of different workstations or clients, but wish to remain
connected and see what they missed while they were away.

You connect to IRC through dircproxy, and it keeps you connected to the
server, even after you detach your client from it. While you're detached,
it logs channel and private messages as well as important events, and
when you reattach it'll let you know what you missed.

%prep
%setup

%build
%configure \
	--enable-poll
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%makeinstall -C src

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog FAQ NEWS PROTOCOL README*
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/dircproxy/

%changelog
* Sun Jan 11 2004 Dag Wieers <dag@wieers.com> - 1.0.5-0
- Initial package. (using DAR)

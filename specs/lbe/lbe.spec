# Authority: dag

# Upstream: Jarek Gawor <gawojar@iit.edu>

%define rname Browser
%define rversion 281

Summary: Excellent LDAP browser and editor.
Name: lbe
Version: 2.8.1
Release: 1
License: Free to use
Group: Applications/System
URL: http://www-unix.mcs.anl.gov/~gawor/ldap/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www-unix.mcs.anl.gov/~gawor/ldapcommon/bin/%{rname}%{rversion}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

Requires: j2re >= 1.2.2

%description
The LDAP Browser/Editor allows users to view the items stored in a LDAP
directory in an hierarchical manner. It also allows modifications of the
LDAP contents if the user is logged in as the Directory Manager. 

The LDAP objects are displayed in the form of a tree and all attributes
of the entries in the form of a table. 

%prep
%setup -n ldapbrowser

%{__cat} <<'EOF' >lbe.sh
#!/bin/sh

if [ ! -d "$JAVA_HOME" ] ; then
	if [ -d "%{_libdir}/jre" ]; then
		JAVA_HOME="%{_libdir}/jre"
	else
		JAVA_HOME="/usr/java"
	fi
fi

if [ ! -d "$HOME/.lbe/" ]; then
	mkdir -p "$HOME/.lbe/"
	cp -a %{_datadir}/lbe/*.{cfg,config} "$HOME/.lbe/"
	ln -sf %{_datadir}/lbe/help/ "$HOME/.lbe/"
	ln -sf %{_datadir}/lbe/templates/ "$HOME/.lbe/"
fi

JNDI_LIB="%{_datadir}/lbe/ldap.jar:%{_datadir}/lbe/jndi.jar:%{_datadir}/lbe/providerutil.jar:%{_datadir}/lbe/ldapbp.jar"
JSSE_LIB="%{_datadir}/lbe/jsse.jar:%{_datadir}/lbe/jnet.jar:%{_datadir}/lbe/jcert.jar"

cd "$HOME/.lbe/"
exec ${JAVA_HOME}/bin/java -cp ".:${JNDI_LIB}:${JSSE_LIB}:%{_datadir}/lbe/browser.jar" lbe.ui.BrowserApp
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_datadir}/lbe/help/ \
			%{buildroot}%{_datadir}/lbe/templates/ \
			%{buildroot}%{_bindir}
%{__install} -m0755 lbe.sh %{buildroot}%{_datadir}/lbe/
%{__ln_s} -f %{_datadir}/lbe/lbe.sh %{buildroot}%{_bindir}/lbe

%{__install} -m0644 *.cfg* *.config* %{buildroot}%{_datadir}/lbe/
%{__install} -m0644 help/*.html %{buildroot}%{_datadir}/lbe/help/
%{__install} -m0644 lib/*.jar %{buildroot}%{_datadir}/lbe/
%{__install} -m0644 *.jar %{buildroot}%{_datadir}/lbe/
%{__install} -m0644 templates/* %{buildroot}%{_datadir}/lbe/templates/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES.TXT LICENSE* *.html
%{_bindir}/*
%{_datadir}/lbe/

%changelog
* Tue Sep 02 2003 Dag Wieers <dag@wieers.com> - 2.8.1-1
- Fixed help and templates.

* Mon Sep 01 2003 Dag Wieers <dag@wieers.com> - 2.8.1-0
- Initial package. (using DAR)

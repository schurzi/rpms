# $Id: gwenview.spec,v 1.2 2004/02/27 17:08:23 driesve Exp $

# Authority: dries

Summary: An image viewer for KDE.
Name: gwenview
Version: 1.0.1
Release: 1
License: GPL
Group: Graphics/Viewers
URL: http://gwenview.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://prdownloads.sourceforge.net/gwenview/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++, XFree86-devel, qt-devel
Requires: kdelibs

#(d) primscreenshot: http://gwenview.sourceforge.net/screenshots/shots/thumbs/6.png
#(d) screenshotsurl: http://gwenview.sourceforge.net/screenshots/

%description
Gwenview can load and save all image formats supported by KDE and 
also browse GIMP files (*.xcf). It can also show meta-information and zoom
images to any size. 

%description -l nl
Gwenview is een image viewer die de formaten ondersteund door KDE kan openen
en bewaren. Ook kan het GIMP bestanden (*.xcf) openen. Het kan ook meta
informatie tonen en zoomen.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
. /etc/profile.d/qt.sh
%configure
make

%install
. /etc/profile.d/qt.sh
echo RPM_BUILD_ROOT is $RPM_BUILD_ROOT
export DESTDIR=$RPM_BUILD_ROOT
make install

%files
%defattr(-,root,root, 0755)
%doc README AUTHORS COPYING CREDITS NEWS TODO
/usr/bin/gwenview
/usr/share/applications/kde/gwenview.desktop
/usr/share/apps/gwenview
/usr/share/apps/konqueror/servicemenus/konqgwenview.desktop
/usr/share/icons/*/*/apps/gwenview.png
/usr/share/locale/*/LC_MESSAGES/gwenview.mo
/usr/share/man/man1/gwenview.1.gz


%changelog
* Tue Jan 27 2004 Dries Verachtert <dries@ulyssis.org> 1.0.1-1
- update to version 1.0.1

* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 1.0.0-2
- completion of spec file (descriptions)
- added some BuildRequires

* Sun Dec 7 2003 Dries Verachtert <dries@ulyssis.org> 1.0.0-1
- first packaging for Fedora Core 1

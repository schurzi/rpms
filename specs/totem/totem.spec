# $Id: totem.spec,v 1.1 2004/02/26 17:54:31 thias Exp $

%{?_without_gstreamer:  %{expand: %%define gstreamer 0}}
%{!?_without_gstreamer: %{expand: %%define gstreamer 1}}

Summary: Movie player for GNOME 2 based on the xine engine
Name: totem
Version: 0.99.9
Release: 1.fr
License: GPL
Group: Applications/Multimedia
URL: http://www.hadess.net/totem.php3
Source: http://www.hadess.net/files/software/totem/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: gnome-desktop >= 2.1.0
Requires: xine-lib >= 1.0.0
%{!?_without_lirc:Requires: lirc}
BuildRequires: gcc-c++, pkgconfig, gettext, scrollkeeper
BuildRequires: xine-lib-devel >= 1.0.0
BuildRequires: gnome-desktop-devel >= 2.0.0, gnome-vfs2-devel, libglade2-devel
BuildRequires: perl-XML-Parser
%{!?_without_lirc:BuildRequires: lirc}

%description
Totem is simple movie player for the Gnome desktop based on xine. It features a
simple playlist, a full-screen mode, seek and volume controls, as well as
a pretty complete keyboard navigation.

Available rpmbuild rebuild options :
--with : gstreamer
--without : lirc


%if %{gstreamer}
%package gstreamer
Summary: Movie player for GNOME 2 based on the GStreamer engine
Group: Applications/Multimedia
Requires: %{name} = %{version}
Requires: gstreamer-plugins >= 0.7.4
BuildRequires: gstreamer-plugins-devel >= 0.7.4

%description gstreamer
Totem is simple movie player for the Gnome desktop. It features a simple
playlist, a full-screen mode, seek and volume controls, as well as a pretty
complete keyboard navigation.

Install this package to use totem with the GStreamer backend instead of the
xine one. You can still use the xine backend by running "totem --xine".
%endif


%prep
%setup -q

%build
%if %{gstreamer}
%configure \
    --enable-gstreamer \
    %{?_without_lirc:--disable-lirc}
make %{?_smp_mflags}
# Move the binary out of the way and cleanup for the xine build
mv src/%{name} src/%{name}-gstreamer
make clean
%endif

%configure \
    %{?_without_lirc:--disable-lirc}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall
%find_lang %{name}
%if %{gstreamer}
# Install the GStreamer version
install -m 755 src/%{name}-gstreamer %{buildroot}%{_bindir}/%{name}-gstreamer
# Rename the xine version
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}-xine
# Make the wrapper script
cat > %{buildroot}%{_bindir}/%{name} << 'EOF'
#!/bin/sh

if [ -x %{_bindir}/%{name}-gstreamer -a ! "$1" = "--xine" ]; then
    %{_bindir}/%{name}-gstreamer "$@"
elif [ -x %{_bindir}/%{name}-xine ]; then
    [ "$1" = "--xine" ] && shift
    %{_bindir}/%{name}-xine "$@"
else
    echo "No %{name}-xine or %{name}-gstreamer found in %{_bindir}."
    exit 1
fi
EOF
chmod 755 %{buildroot}%{_bindir}/%{name}
%endif

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
    %{_sysconfdir}/gconf/schemas/totem.schemas \
    %{_sysconfdir}/gconf/schemas/totem-video-thumbnail.schemas >/dev/null || :

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/%{name}
%{_bindir}/%{name}-video-thumbnailer
%{_bindir}/vanity
%if %{gstreamer}
%{_bindir}/%{name}-xine
%endif
%{_libdir}/bonobo/servers/*.server
%{_libexecdir}/%{name}-properties-page
%{_datadir}/application-registry/%{name}.applications
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/vanity.desktop
%{_datadir}/gnome/help/%{name}
%{_datadir}/mime-info/%{name}.keys
%{_datadir}/omf/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/%{name}

%if %{gstreamer}
%files gstreamer
%defattr(-, root, root)
%{_bindir}/%{name}-gstreamer
%endif

%changelog
* Fri Feb 13 2004 Matthias Saou <http://freshrpms.net/> 0.99.9-1.fr
- Update to 0.99.9, rebuild against gstreamer 0.7.4.
- New required perl-XML-Parser build dep (!?).
- Added missing defattr for the gstreamer sub-package.

* Mon Dec  1 2003 Matthias Saou <http://freshrpms.net/> 0.99.8-2.fr
- Disable the obsolete xinitthreads patch.

* Thu Nov 13 2003 Matthias Saou <http://freshrpms.net/> 0.99.8-1.fr
- Update to 0.99.8.
- Added help and omf files.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.99.7-2.fr
- Rebuild for Fedora Core 1.

* Thu Oct 16 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.99.7.

* Tue Oct 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.99.6.
- Added missing build dependencies, thanks to mach.

* Mon Sep 15 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.99.5.
- Now default to build the gstreamer package too.

* Thu Sep  4 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.99.4.
- Add if to the sub-package description to avoid build dep problem.

* Sun Jul 27 2003 Peter Oliver <rpms@mavit.freeserve.co.uk> 0.99.2-4.fr
- Fixed wrapper's handling of spaces in filenames.

* Wed Jul  9 2003 Matthias Saou <http://freshrpms.net/>
- Added gstreamer build option and sub-package + wrapper script.

* Tue Jul  8 2003 Matthias Saou <http://freshrpms.net/>
- Added an updated patch since the problem was in fact *not* fixed.

* Sat Jul  5 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.99.2.
- Removed the xinit threads patch.

* Sun Jun 22 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.99.1.

* Wed May 28 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.99.0.
- Added --without lirc build option.
- Added gnome-desktop-devel build dep and vanity desktop file.

* Sun May 11 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.98.0.
- Included new bonobo files.

* Tue Apr 29 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.97.0.
- Added xinitthreads patch to fix potential hang.

* Thu Apr 10 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.96.0.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Feb 22 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.95.1.

* Thu Jan 30 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.90.0.
- Requirements (glib, libgnomeui) are too recent for Red Hat Linux 8.0.

* Wed Oct 30 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.0.
- Added the new xineplug_inp_gnomevfs modules.

* Mon Sep 30 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.


# Authority: dag

### FIXME: Makefile uses gcc hardcoded
# Distcc: 0
#
### FIXME: Makefile creates symlinks to outside buildroot
# Soapbox: 0

%define rname Gemu

Summary: GNOME EMU10K1 configuration tool.
Name: gemu
Version: 0.8
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://www.roadfeldt.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: http://prdownloads.sourceforge.net/gemu/%{name}-%{version}.tar.gz
Source1: http://prdownloads.sourceforge.net/emu10k1/emu10k1-v0.20a.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
The purpose of Gemu is to control sound cards based on the EMU10K1
platform. It is meant to allow control to all aspects of EMU10K1 based
sound cards. Features include route creation, effect/patch control, misc. 
card settings, route volume mixer, source and destination mixers, and OSS 
Mixer binding.

%prep
%setup -n %{rname}-%{version} -a 1
#%setup -n %{rname}-%{version}

%build
(cd emu10k1-v0.20a; %{__make}; %{__make} tools)
#cd emu10k1-v0.20a
#%{__make}
#%{__make} tools
#cd -
%configure 
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/gemu
%{_datadir}/gnome/apps/Multimedia/*.desktop

%changelog
* Wed May 28 2003 Dag Wieers <dag@wieers.com> - 0.8-0
- Initial package. (using DAR)

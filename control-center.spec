# Note that this is NOT a relocatable package
%define prefix   /usr

%define ccsingle control-center-single-0.2

Summary: The GNOME Control Center.
Name: control-center
Version: 1.4.0.1
Release: 12
Epoch: 1
License: GPL/LGPL
Group: User Interface/Desktops
Source: ftp://ftp.gnome.org/pub/control-center-%{version}.tar.gz

Source1: control-center.png
Source2: gnomecc.desktop
#Source3: background-properties-new.tar.gz
Source10: control-center-1.2.1-ja.po
Source11: control-center-po.tar.gz
Source12: %{ccsingle}.tar.gz

BuildPrereq: gdk-pixbuf
BuildRoot: %{_tmppath}/control-center-%{PACKAGE_VERSION}-root
BuildRequires: gdk-pixbuf-devel
BuildRequires: gnome-libs-devel
BuildRequires: gnome-vfs-devel
BuildRequires: libxml-devel

Obsoletes: gnome
Requires: /bin/aumix-minimal

URL: http://www.gnome.org

Patch: control-center-nosound.patch
Patch1: control-center-esdrelease.patch
Patch3: control-center-fsbgpath.patch
#Patch4: control-center-1.0.5-dontstartesd.patch
#Patch5: control-center-1.0.5-newsession.patch
#Patch6: control-center-1.0.5-fixclosedlg.patch 
Patch7: control-center-1.2.0-limitedbgs.patch

#Patch8: control-center-1.0.5-smfixtry.patch

#Patch22: control-center-1.0.5-warning.patch
#Patch23: control-center-1.0.7pre-cappletrace.patch
#Patch24: control-center-fixrevert.patch

Patch25: control-center-1.4.0.1-bgcolor1.patch
#Patch26: control-center-1.2.0-switch.patch
Patch27: control-center-1.2.0-history.patch
#Patch28: control-center-1.2.0-themesafety.patch
Patch29: control-center-1.2.0-wmaker.patch
Patch30: control-center-1.2.1-bigbg.patch
#Patch31: control-center-1.2.1-noread.patch
#Patch32: control-center-1.2.1-solidbg.patch
#Patch33: control-center-1.2.2-fvwm2.patch
# Japanese patch
#Patch40: control-center-1.2.1-jp.patch
# Korean-related patch (?) bug #23782
#Patch41: control-center-1.2.2-fontset.patch
Patch50: control-center-mixer.patch
Patch51: control-center-xscreensaver-dpms.patch
Patch52: control-center-1.4.0.1-multifix.patch
Patch53: control-center-1.4.0.1-nocapplet.patch
Patch54: control-center-1.4.0.1-correct_config.patch
Requires: xscreensaver >= 3.32

%description
GNOME (the GNU Network Object Model Environment) is an attractive and
easy-to-use GUI desktop environment. The control-center package
provides the GNOME Control Center utilities that allow you to setup
and configure your system's GNOME environment (things like the desktop
background and theme, the screensaver, the window manager, system
sounds, and mouse behavior).

If you install GNOME, you need to install control-center.

%package devel
Summary: The GNOME Control Center development environment.
Group: Development/Libraries
Requires: control-center = %{PACKAGE_VERSION}
Requires: gnome-libs-devel

%description devel
The control-center-devel package contains the development environment
needed for creating the capplets used in the GNOME Control
Center.

If you are interested in developing capplets for the GNOME control
center, you need to install this package. If you use the GNOME
desktop, but you are not developing applications, you do not need to
install this package.

%prep
%setup -q -a 12

#(cd $RPM_BUILD_DIR/control-center-%{PACKAGE_VERSION}/capplets &&
# tar xfz %{SOURCE3})
# our translations
tar zxf %{SOURCE11}

%patch -p1 -b .nosound
%patch1 -p1 -b .esdrelease
%patch3 -p1 -b .fsbgpath
#%patch4 -p1 -b .dontstartesd
#%patch5 -p1 -b .newsession
#%patch6 -p1 -b .fixclosedlg
%patch7 -p1 -b .limitedbgs
#%patch8 -p1 -b .smfixtry

#%patch22 -p1 -b .warning
#%patch23 -p1 -b .cappletrace
#%patch24 -p1 -b .fixrevert

%patch25 -p1 -b .bgcolor1

#%patch26 -p1 -b .switch
#%patch27 -p1 -b .history
#%patch28 -p1 -b .themesafety
%patch29 -p1 -b .wmaker
%patch30 -p1 -b .bigbg
#%patch31 -p1 -b .noread
#%patch32 -p1 -b .solidbg
#%patch33 -p1 -b .fvwm2
#%patch40 -p1 -b .jp
#%patch41 -p1 -b .fontset
%patch50 -p1 -b .mixer
%patch51 -p1 -b .dpms
%patch52 -p1 -b .multifix
%patch53 -p1 -b .nocapplet
%patch54 -p1 -b .correct_config

automake

# install new desktop entry and icon
cp %{SOURCE1} $RPM_BUILD_DIR/control-center-%{PACKAGE_VERSION}/control-center
cp %{SOURCE2} $RPM_BUILD_DIR/control-center-%{PACKAGE_VERSION}/control-center
cp %{SOURCE10} $RPM_BUILD_DIR/control-center-%{PACKAGE_VERSION}/po/ja.po

%build

CFLAGS="$RPM_OPT_FLAGS" %configure --sysconfdir=/etc
make

cd %{ccsingle} 
automake
autoconf
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall} sysconfdir=$RPM_BUILD_ROOT/etc

# clear out ui props for now
#rm -f $RPM_BUILD_ROOT%{prefix}/bin/ui-properties
#rm -rf $RPM_BUILD_ROOT%{prefix}/share/control-center/UIOptions
#rm -rf $RPM_BUILD_ROOT%{prefix}/share/gnome/apps/Settings/UIOptions

# get rid of this, so it won't show up in panel menu. use start here 
# instead.
rm -f $RPM_BUILD_ROOT%{prefix}/share/gnome/apps/Settings/gnomecc.desktop

cd %{ccsingle}
%makeinstall sysconfdir=$RPM_BUILD_ROOT/etc

cd $RPM_BUILD_DIR/%{name}-%{version}

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README
%{prefix}/bin/*
%{prefix}/lib/lib*.so.*
%config /etc/CORBA/servers/*
%{prefix}/share/control-center
%{prefix}/share/pixmaps/*
%{prefix}/share/gnome/wm-properties/*
%{prefix}/share/gnome/apps/Settings/*
%{prefix}/share/gnome/help/control-center/*

%files devel
%defattr(-, root, root)

%{prefix}/lib/lib*.so
%{prefix}/lib/*a
%{prefix}/lib/*Conf.sh
%{prefix}/share/idl
%{prefix}/include/*

%changelog
* Wed Aug 01 2001 Havoc Pennington <hp@redhat.com>
- remove .desktop file for gnomecc, so it won't appear 
  in panel menu, #49653

* Mon Jul 30 2001 Jonathan Blandford <jrb@redhat.com>
- allow to build without depending on control-center-devel

* Mon Jul 23 2001 Jonathan Blandford <jrb@redhat.com>
- Add BuildRequires

* Mon Jul 16 2001 Jonathan Blandford <jrb@redhat.com>
- New version of control-center-single

* Thu Jul 12 2001 Alexander Larsson <alexl@redhat.com>
- Change default background to the same as the nautilus one

* Mon Jul 09 2001 Havoc Pennington <hp@redhat.com>
- add hack to default to standalone control panels

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Tue May 22 2001 Havoc Pennington <hp@redhat.com>
- putting in tree for David

* Tue May 22 2001 David Sainty <dsainty@redhat.com>
- improve DPMS patch for the try case, and enable patch

* Wed May  2 2001 Bill Nottingham <notting@redhat.com>
- add patch to use xscreensaver's DPMS stuff, require that version

* Fri Apr 20 2001  <jrb@redhat.com>
- New Version (1.4.0.1)

* Wed Apr  4 2001 Bill Nottingham <notting@redhat.com>
- kick the mixer once on startup if we aren't running esd

* Thu Mar 15 2001 Havoc Pennington <hp@redhat.com>
- translations

* Thu Mar 01 2001 Owen Taylor <otaylor@redhat.com>
- Rebuild for GTK+-1.2.9 include paths

* Fri Feb 23 2001 Trond Eivind Glomsrød <teg@redhat.com>
- langify
- don't define and use "ver" at the top of the file
- move changelog to sane location

* Thu Feb 08 2001 Elliot Lee <sopwith@redhat.com> 1.2.2-4
- Apply patch from bug #23782 to see how it works

* Fri Feb 02 2001 Elliot Lee <sopwith@redhat.com> 1.2.2-3
- Include fvwm2.desktop in WM's

* Sat Jan 27 2001 Akira TAGOH <tagoh@redhat.com>
- Added Japanese patch.

* Mon Dec 04 2000 Jonathan Blandford <jrb@redhat.com>
- Update release.

* Sun Aug 13 2000 Owen Taylor <otaylor@redhat.com>
- Again, fix problem with solid backgrounds in bg-properties capplet
  (patch got lost somewhere) 

* Fri Aug 11 2000 Jonathan Blandford <jrb@redhat.com>
- Up Epoch and release

* Thu Aug 10 2000 Owen Taylor <otaylor@redhat.com>
- Handle unreadable desktop files without crashing

* Mon Aug 07 2000 Owen Taylor <otaylor@redhat.com>
- Fix problem with backgrounds bigger than screen.

* Tue Aug 01 2000 Owen Taylor <otaylor@redhat.com>
- Fix problem when ~/.gtkrc does not already exist.
- Fix problem with solid backgrounds in bg-properties capplet

* Tue Jul 18 2000 Owen Taylor <otaylor@redhat.com>
- Sort of fix problem with people hitting OK while the 
  "Save Session" dialog is still up. (Session won't be saved, 
  but at least the selected entry will be correctly kept.)
- Fix history list in background properties capplet
- Fix problems with temporary files in theme-selector capplet

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun 19 2000 Owen Taylor <otaylor@redhat.com>
- Require redhat-logos
- Some spec file and FHS fixes
- reposition embedded logo a bit

* Mon Jun 19 2000 Owen Taylor <otaylor@redhat.com>
- Add big change to use gdk-pixbuf for backgrounds and add
  the ability to emboss the background with a logo

* Mon Feb 28 2000 Preston Brown <pbrown@redhat.com>
- revert .so strip

* Thu Feb 03 2000 Preston Brown <pbrown@redhat.com>
- strip .so lib
- use configure macro

* Mon Sep 20 1999 Jonathan Blandford <jrb@redhat.com>
- changed to work with 1.0.40

* Fri Sep 17 1999 Jonathan Blandford <jrb@redhat.com>
- Added fixrevert bug to fix bug in theme selector.

* Sun Jun 13 1999 Jonathan Blandford <jrb@redhat.com>
- updated RPM to use new control-center.

* Wed Apr 07 1999 Michael Fulbright <drmike@redhat.com>
- fixed sound-properties to only disable sound when run with --init-settings-..
- removed debugging output from several capplets, fixed try behaviour of sm and
  gnome-edit capplets
- fixed bug in screensaver and background props
- added new icons

* Mon Apr 05 1999 Jonathan Blandford <jrb@redhat.com>
- added a patch to fix the close dialog
- added a patch to limit the number of bg's in the history.

* Fri Apr 02 1999 Jonathan Blandford <jrb@redhat.com>
- vesion 1.0.5
- removed all patches >10 other then dontstartesd.

* Thu Apr 01 1999 Michael Fulbright <drmike@redhat.com>
- removed UI props till it works better

* Wed Mar 31 1999 Michael Fulbright <drmike@redhat.com>
- make sure we DONT inadvertantly start esd by calling esd_open_...

* Tue Mar 30 1999 Michael Fulbright <drmike@redhat.com>
- changed default bg color to '#356390'

* Thu Mar 25 1999 Michael Fulbright <drmike@redhat.com>
- prime file selector path for browse in background-props if 
  "/usr/share/pixmaps/backgrounds/" exists.
- fix behavior of file selector when you delete/cancel/ok it

* Wed Mar 24 1999 Michael Fulbright <drmike@redhat.com>
- added patch to fix trying in theme selector 
- disabled crystal screensaver, it does evil things to preview in capplet

* Mon Mar 22 1999 Michael Fulbright <drmike@redhat.com>
- version 1.0.4, fixes problems with sndprops and theme props among
  other things.

* Thu Mar 18 1999 Michael Fulbright <drmike@redhat.com>
- fix sound-properties capplet so Try/Revert doesnt come on unless user
  changes something
- fixed theme-selector to not leave processes behind on Linux 2.2 kernels
- strip binaries

* Sun Mar 14 1999 Michael Fulbright <drmike@redhat.com>
- version 1.0.3
- added patch to make esd release after 30 sec of inactivity

* Wed Mar 10 1999 Michael Fulbright <drmike@redhat.com>
- version 1.0.2
- turned off sound by default

* Thu Mar 04 1999 Michael Fulbright <drmike@redhat.com>
- version 1.0.1

* Mon Feb 15 1999 Michael Fulbright <drmike@redhat.com>
- version 0.99.8.1
- added etc/CORBA/servers/* to file list

* Fri Feb 12 1999 Michael Fulbright <drmike@redhat.com>
- update to 0.99.8
- added /usr/lib/cappletConf.sh

* Mon Feb 08 1999 The Rasterman <raster@redhat.com>
- update to 0.99.5.1

* Wed Feb 03 1999 Michael Fulbright <drmike@redhat.com>
- update to 0.99.5

* Mon Jan 20 1999 Michael Fulbright <drmike@redhat.com>
- update to 0.99.3.1

* Mon Jan 18 1999 Michael Fulbright <drmike@redhat.com>
- update to 0.99.3
- seems like patch for non-standard xscreensaver placement was already in
  prestine sources(?)

* Wed Jan 06 1999 Jonathan Blandford <jrb@redhat.com>
- updated to 0.99.1
- temporary hack patch to get path to work to non-standard placement
  of xscreensaver binaries in RH 5.2

* Wed Dec 16 1998 Jonathan Blandford <jrb@redhat.com>
- Created for the new control-center branch


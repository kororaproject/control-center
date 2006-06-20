%define gettext_package control-center-2.0

%define pango_version 1.0.99.020703
%define gtk2_version 2.6.0
%define gconf2_version 1.2.0
%define gnome_desktop_version 2.3.0
%define libgnome_version 2.3.0
%define libbonobo_version 2.3.0
%define libgnomeui_version 2.3.0
%define libbonoboui_version 2.3.0
%define gnome_vfs2_version 2.3.0
%define desktop_file_utils_version 0.9
%define xft_version 2.1.7
%define fontconfig_version 1.0.0
%define redhat_menus_version 1.8
%define metacity_version 2.5.3
%define libxklavier_version 1.14
%define gnome_menus_version 2.11.1
%define usermode_version 1.83

Summary: GNOME Control Center
Name: control-center
Version: 2.15.3
Release: 3
Epoch: 1
License: GPL/LGPL
Group: User Interface/Desktops
Source: ftp://ftp.gnome.org/pub/GNOME/sources/control-center/2.14/control-center-%{version}.tar.bz2
Source2: ftp://ftp.gnome.org/pub/GNOME/sources/control-center/2.12/control-center-2.12.3.tar.bz2

Patch1: control-center-2.13.90-fedora-apps.patch
Patch2: control-center-2.9.4-filesel.patch
Patch3: control-center-2.10.1-mark-tool-buttons-important.patch
Patch4: control-center-2.13.90-about-me-faces.patch
Patch5: control-center-2.12.0-run-power-manager.patch
Patch6: control-center-2.12.1-passwd.patch
Patch7: control-center-2.14.2-gecos.patch
Patch8: control-center-2.13.5-m4.patch
Patch10: background-no-delay.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL: http://www.gnome.org

Obsoletes: gnome fontilus
# the background capplets expects its .xml files in 
# a different place now
Conflicts: desktop-backgrounds-basic < 2.0-27
Conflicts: desktop-backgrounds-extended < 2.0-27
Requires: redhat-menus >= %{redhat_menus_version}
Requires: gnome-icon-theme
Requires: libxklavier >= %{libxklavier_version}
Requires: libgail-gnome
Requires: alsa-lib
Requires: gnome-menus >= %{gnome_menus_version}
PreReq:   gtk2
Requires: usermode >= %{usermode_version}

BuildRequires: autoconf automake libtool
BuildRequires: esound-devel
BuildRequires: pango-devel >= %{pango_version}
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: GConf2-devel >= %{gconf2_version}
BuildRequires: gnome-desktop-devel >= %{gnome_desktop_version}
BuildRequires: libgnomeui-devel >= %{libgnomeui_version}
BuildRequires: libgnome-devel >= %{libgnome_version}
BuildRequires: libbonobo-devel >= %{libbonobo_version}
BuildRequires: libbonoboui-devel >= %{libbonoboui_version}
BuildRequires: gnome-vfs2-devel >= %{gnome_vfs2_version}
BuildRequires: bonobo-activation-devel
BuildRequires: fontconfig-devel >= %{fontconfig_version}
BuildRequires: desktop-file-utils >= %{desktop_file_utils_version}
BuildRequires: /usr/bin/automake-1.4
BuildRequires: /usr/bin/autoconf
BuildRequires: metacity >= %{metacity_version}
BuildRequires: libxklavier-devel >= %{libxklavier_version}
BuildRequires: libXcursor-devel
BuildRequires: alsa-lib-devel
BuildRequires: nautilus
BuildRequires: eel2-devel
BuildRequires: gettext
BuildRequires: gnome-menus-devel >= %{gnome_menus_version}
# For intltool:
BuildRequires: perl-XML-Parser >= 2.31-16
BuildRequires: evolution-data-server-devel
BuildRequires: libXxf86misc-devel 
BuildRequires: libxkbfile-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: gnome-doc-utils
BuildRequires: gstreamer-devel
BuildRequires: gstreamer-plugins-base
BuildRequires: libglade2-devel
BuildRequires: libxml2-devel
BuildRequires: hal-devel >= 0.5.6
BuildRequires: dbus-devel >= 0.32

%description
GNOME (the GNU Network Object Model Environment) is an attractive and
easy-to-use GUI desktop environment. The control-center package
provides the GNOME Control Center utilities that allow you to setup
and configure your system's GNOME environment (things like the desktop
background and theme, the screensaver, system sounds, and mouse
behavior).

If you install GNOME, you need to install control-center.

%package devel
Summary: GNOME Control Center development libraries and header files
Group: Development/Libraries
Requires: %{name} = %{?epoch}:%{version}-%{release}

%description devel
GNOME (the GNU Network Object Model Environment) is an attractive and
easy-to-use GUI desktop environment. The control-center package
provides the GNOME Control Center utilities that allow you to setup
and configure your system's GNOME environment (things like the desktop
background and theme, the screensaver, system sounds, and mouse
behavior).

This packages development files for GNOME Control Center.

%prep
%setup -q

tar xjf %{SOURCE2}
rm -rf capplets/background
cp -R control-center-2.12.3/capplets/background capplets

%patch1 -p1 -b .fedora-apps
%patch2 -p1 -b .filesel
%patch3 -p1 -b .mark-tool-buttons-important
%patch4 -p1 -b .about-me-faces
%patch5 -p1 -b .run-power-manager
%patch6 -p1 -b .passwd
%patch7 -p1 -b .gecos
%patch8 -p1 -b .m4
%patch10 -p1 -b .no-delay

%build

# Rerun autoheader because of help-left-handled-dual-mice-users patch
autoheader

# Rerun autoconf because of 
# help-left-handled-dual-mice-users patches
autoconf

# Run aclocal and automake for run-power-manager
aclocal
automake

# work around a gstreamer problem where it doesn't find
# plugins the first time around
/usr/bin/gst-inspect-0.10 --print-all

# Add -Wno-error to silence gswitchit
%configure --disable-gstreamer --enable-alsa CFLAGS="$RPM_OPT_FLAGS -Wno-error" --enable-aboutme --disable-scrollkeeper
make

%install
rm -rf $RPM_BUILD_ROOT

export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

desktop-file-install --vendor gnome --delete-original                   \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications			        \
  --add-only-show-in GNOME                                              \
  --add-category X-Red-Hat-Base                                         \
  $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

desktop-file-install --vendor gnome --delete-original                   \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications 			\
  --remove-category X-Red-Hat-Base                                      \
  $RPM_BUILD_ROOT%{_datadir}/applications/gnome-default-applications.desktop

# bug 171059
sed -e 's/=Font$/=Fonts/g' $RPM_BUILD_ROOT%{_datadir}/applications/gnome-font-properties.desktop > \
                           $RPM_BUILD_ROOT%{_datadir}/applications/.gnome-font-properties.desktop.tmp
mv $RPM_BUILD_ROOT%{_datadir}/applications/.gnome-font-properties.desktop.tmp \
   $RPM_BUILD_ROOT%{_datadir}/applications/gnome-font-properties.desktop

# remove control center desktop file
/bin/rm -f $RPM_BUILD_ROOT%{_datadir}/applications/gnomecc.desktop

# desktop-file-install really should not be generating this
/bin/rm -f $RPM_BUILD_ROOT%{_datadir}/applications/mimeinfo.cache

# replace accessibility desktop file
#/bin/rm -f $RPM_BUILD_ROOT%{_datadir}/applications/*accessibility*.desktop
#ln -sf %{_datadir}/desktop-menu-patches/gnome-accessibility.desktop $RPM_BUILD_ROOT%{_datadir}/applications/gnome-accessibility.desktop

cp -f $RPM_BUILD_ROOT%{_datadir}/control-center-2.0/icons/* $RPM_BUILD_ROOT%{_datadir}/pixmaps

# fix installed but not packaged
/bin/rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

/bin/rm -rf $RPM_BUILD_ROOT%{_libdir}/libgnome-window-settings.*a
/bin/rm -rf $RPM_BUILD_ROOT%{_libdir}/gnome-vfs-2.0/modules/*.a
/bin/rm -rf $RPM_BUILD_ROOT%{_libdir}/gnome-vfs-2.0/modules/*.la

# loadable modules don't need static versions or .la files
/bin/rm -f $RPM_BUILD_ROOT%{_libdir}/window-manager-settings/*.*a
/bin/rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-1.0/*.*a

%find_lang %{gettext_package}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
SCHEMAS="apps_gnome_settings_daemon_default_editor.schemas apps_gnome_settings_daemon_keybindings.schemas apps_gnome_settings_daemon_screensaver.schemas apps_gnome_settings_daemon_power_manager.schemas desktop_gnome_font_rendering.schemas desktop_gnome_peripherals_keyboard_xkb.schemas fontilus.schemas themus.schemas"
for S in $SCHEMAS; do
  gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/$S > /dev/null
done
update-desktop-database --quiet %{_datadir}/applications
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%postun
/sbin/ldconfig
update-desktop-database --quiet %{_datadir}/applications
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%files -f %{gettext_package}.lang
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README

%{_datadir}/control-center-2.0
%{_datadir}/pixmaps/*
%{_datadir}/icons/*
%{_datadir}/gnome/*
%{_datadir}/applications/*.desktop
%{_datadir}/idl
%{_datadir}/omf/control-center
%{_datadir}/gnome-default-applications/*
%{_datadir}/desktop-directories/*
%{_bindir}/*
%{_libexecdir}/*
%{_libdir}/bonobo/*
%{_libdir}/nautilus/extensions-1.0/*
%{_libdir}/*.so.*
%{_libdir}/window-manager-settings
%{_sysconfdir}/gconf/schemas/*.schemas
%{_sysconfdir}/gnome-vfs-2.0/modules/*.conf
%{_libdir}/gnome-vfs-2.0/modules/*.so

%files devel
%defattr(-,root,root)
%{_includedir}/gnome-window-settings-2.0
%{_libdir}/libgnome-window-settings.so
%{_libdir}/pkgconfig/gnome-window-settings*

%changelog
* Tue Jun 20 2006 Matthias Clasen  <mclasen@redhat.com> - 2.15.3-3
- Rebuild against new libxklavier

* Wed Jun 14 2006 Tomas Mraz <tmraz@redhat.com>
- rebuilt with new gnutls
- require gstreamer-devel

* Wed Jun 14 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.3-2
- Work around a gstreamer problem

* Tue Jun 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.3-1
- Update to 2.15.3

* Tue Jun  6 2006 Kristian Høgsberg <krh@redhat.com> - 2.14.2-3
- Add devel package.
- Add build requires for autoconf, automake, and libtool.

* Mon May 29 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2-2
- Update to 2.14.2

* Thu May 25 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.1-4
- Add missing buildrequires

* Mon Apr 17 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.1-3
- Fix the thunderbird commandline

* Mon Apr 10 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.1-2
- Update to 2.14.1

* Thu Apr  6 2006 Ray Strode <rstrode@redhat.com> - 2.14.0-2
- add missing build reqs (bug 188167)

* Mon Mar 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.0-1
- Update to 2.14.0

* Wed Feb 15 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.92-2
- Add a missing BuildRequires

* Wed Feb 15 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.92-1
- Update to 2.13.92

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1:2.13.91-1.1
- bump again for double-long bug on ppc(64)

* Wed Feb  8 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.91-1
- Update to 2.13.91
- Reenable Spanish help

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1:2.13.90-6.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Feb  6 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.13.90-6
- Avoid delays when switching backgrounds

* Mon Feb  6 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.13.90-3
- Use the 2.12 background capplet

* Fri Feb  3 2006 Christopher Aillon <caillon@redhat.com> 1:2.13.90-2
- Patch gnome-about-me's file chooser dialog to default to the
  system faces directory

* Mon Jan 30 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.13.90-1
- Update to 2.13.90

* Sat Jan 28 2006 David Malcolm <dmalcolm@redhat.com> - 1:2.13.5.1-2
- rebuild against new e-d-s

* Fri Jan 20 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.13.5.1-1
- Update to 2.13.5.1

* Tue Jan 17 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.13.5-1
- Update to 2.13.5

* Fri Jan 13 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.13.4-2
- Add a build requires for libXcursor-devel, to fix the 
  mouse capplet.

* Wed Jan  4 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.13.4-1
- Update to 2.13.4

* Tue Dec 20 2005 Ray Strode <rstrode@redhat.com> - 1:2.13.3-2
- rebuild 

* Wed Dec 14 2005 Matthias Clasen <mclasen@redhat.com> - 1:2.13.3-1
- Update to 2.13.3
- Update patches

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Dec  2 2005 Matthias Clasen <mclasen@redhat.com> - 1:2.13.2-1
- Update to 2.13.2

* Mon Nov 14 2005 Matthias Clasen <mclasen@redhat.com> - 1:2.12.1-4
- Reenable about me capplet
- Add a preview to the user image chooser
- Make about me capplet use userpasswd for passwords and userinfo for
  gecos information

* Mon Oct 24 2005 Matthias Clasen <mclasen@redhat.com> - 1:2.12.1-3
- Support a gconf key to hide the input method menu

* Wed Oct 19 2005 Ray Strode <rstrode@redhat.com> - 1:2.12.1-2
- rename Font capplet to Fonts (bug 171059)

* Thu Oct  6 2005 Matthias Clasen <mclasen@redhat.com> - 1:2.12.1-1
- Update to 2.12.1

* Fri Sep 23 2005 Ray Strode <rstrode@redhat.com> - 1:2.12.1-4
- remove explicit dependency on xscreensaver

* Wed Sep 21 2005 Ray Strode <rstrode@redhat.com> - 1:2.12.1-3
- run gnome-power-manager if available

* Wed Sep 14 2005 Ray Strode <rstrode@redhat.com> - 1:2.12.1-2
- new patch for left-handed mode

* Wed Sep  7 2005 Matthias Clasen <mclasen@redhat.com> - 1:2.12.0-1
- Update to 2.12.0
- Drop upstreamed patches

* Wed Aug 31 2005 Ray Strode <rstrode@redhat.com> - 1:2.11.91-4
- Potentially fix tablet bustage (bug 167227)

* Tue Aug 23 2005 Ray Strode <rstrode@redhat.com> - 1:2.11.91-3
- Configure all mice for left-handed mode in left-handed 
  mode (bug 126420)
- dont use pango-xft when drawing keyboard layout in 
  gnome-keyboard-properties dialog

* Tue Aug 16 2005 Warren Togami <wtogami@redhat.com> - 1:2.11.91-2
- rebuild for new cairo

* Wed Aug 10 2005 Ray Strode <rstrode@redhat.com> - 1:2.11.91-1
- New upstream version
- Patch out buildreq for e-d-s (bug 165493)

* Tue Aug  9 2005 David Malcolm <dmalcolm@redhat.com> - 1:2.11.90-2
- rebuild (against new evolution-data-server-devel)

* Wed Aug  3 2005 Matthias Clasen <mclasen@redhat.com> - 1:2.11.90-1
- New upstream version

* Fri Jul 15 2005 Matthias Clasen <mclasen@redhat.com> - 1:2.11.6-1
- New upstream version

* Thu Jul 14 2005 Matthias Clasen <mclasen@redhat.com> - 1:2.11.5-2
- Disable the about-me capplet 

* Fri Jul  8 2005 Matthias Clasen <mclasen@redhat.com> - 1:2.11.5-1
- Update to 2.11.5

* Mon May 23 2005 Bill Nottingham <notting@redhat.com> - 1:2.10.1-6
- don't ship static versions of nautilus extensions

* Thu May  5 2005 Ray Strode  <rstrode@redhat.com> - 1:2.10.1-5
- Don't pop up accessibility dialogs under currently focused
  window

* Wed Apr 27 2005 Jeremy Katz <katzj@redhat.com> - 1:2.10.1-4
- run gtk-update-icon-cache with -q 

* Mon Apr 25 2005 Matthias Clasen <mclasen@redhat.com> - 2.10.1-3
- Avoid a warning from gnome-default-applications-properties.

* Fri Apr 15 2005 Ray Strode <rstrode@redhat.com> 2.10.1-2
- Show preferred text toolbar items in ui-properties capplet
  preview (bug 154836)

* Fri Apr 8 2005 Ray Strode <rstrode@redhat.com> 2.10.1-1
- Update to 2.10.1

* Wed Mar 30 2005 Warren Togami <wtogami@redhat.com> 2.10.0-4
- fix ldconfig (#152575)

* Mon Mar 28 2005 Christopher Aillon <caillon@redhat.com>
- rebuilt

* Fri Mar 25 2005 Christopher Aillon <caillon@redhat.com> 2.10.0-2
- Update the GTK+ theme icon cache on (un)install

* Thu Mar 17 2005 Ray Strode <rstrode@redhat.com> - 2.10.0-1
- Update to upstream version 2.10.0
- Add some -Wno-error foo to calm gswitchit

* Fri Feb 11 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.91-1
- Update to 2.9.91

* Thu Feb  3 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.4-5
- Fix the conflict to be against the actual packages

* Wed Feb  2 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.4-4
- Call update-desktop-database in %%post

* Wed Feb  2 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.4-3
- Add a Conflicts against older desktop-backgrounds, since
  the location of the xml background descriptions has changed

* Wed Feb  2 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.4-2
- Make the background filechooser open in the right directory

* Tue Feb  1 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.4-1
- Update to 2.9.4
- Drop upstreamed patches

* Wed Oct 13 2004 Marco Pesenti Gritti <mpg@redhat.com>
- #134670 Install icon theme untars it into $HOME/.themes

* Mon Oct 11 2004 Warren Togami <wtogami@redhat.com> - 1:2.8.0-11
- #135219 Preferred Applications hardcoded evolution-1.6
- Add Opera as browser and mail client

* Wed Oct 06 2004 Warren Togami <wtogami@redhat.com> - 1:2.8.0-9
- #109738 Again Fix Preferred Applications url handler keys

* Mon Sep 27 2004 Matthias Clasen <mclasen@redhat.com> - 1:2.8.0-8
- make the preview resize less

* Fri Sep 24 2004 Ray Strode <rstrode@redhat.com> - 1:2.8.0-7
- Remove X-Red-Hat-Base from Preferred Apps instead of Settings

* Fri Sep 24 2004 Ray Strode <rstrode@redhat.com> - 1:2.8.0-6
- require latest version of redhat-menus

* Fri Sep 24 2004 Matthias Clasen <mclasen@redhat.com> - 1:2.8.0-5
- add a preview to the background file chooser.

* Fri Sep 24 2004 Ray Strode <rstrode@redhat.com> - 1:2.8.0-4
- Delete control center desktop file
- Remove superfluous args to second desktop-file-install command

* Thu Sep 23 2004 Ray Strode <rstrode@redhat.com> - 1:2.8.0-3
- Require a working version of desktop-file-install

* Thu Sep 23 2004 Ray Strode <rstrode@redhat.com> - 1:2.8.0-2
- add everything but Preferred Applications entry back to Preferences
  menu (woops)

* Wed Sep 22 2004 GNOME <jrb@redhat.com> - 1:2.8.0-1
- new version; disable gstreamer and enable alsa

* Mon Sep 20 2004 Ray Strode <rstrode@redhat.com> - 1:2.7.1-4
- remove Preferred Applications entry from Preferences menu

* Tue Sep  7 2004 Matthias Clasen <mclasen@redhat.com> - 1:2.7.1-3
- don't show hyper if its mapped to super (#131635)

* Thu Sep  2 2004 GNOME <jrb@redhat.com> - 1:2.7.1-2
- fix help

* Sun Aug 29 2004 Jonathan Blandford <jrb@redhat.com> 1:2.7.1-1
- new version

* Mon Aug  9 2004 Jonathan Blandford <jrb@redhat.com> 1:2.7.0-1
- update to 2.7.0

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 05 2004 Warren Togami <wtogami@redhat.com> 1:2.6.1-3
- workaround "evolution-1.6" bug, always point at /usr/bin/evolution
- Preferred Applications should be visible from KDE

* Tue Apr 20 2004 Jeremy Katz <katzj@redhat.com> 1:2.6.1-1
- update to 2.6.1 to fix xorg brokenness

* Thu Apr 15 2004 Alexander Larsson <alexl@redhat.com> 1:2.6.0.3-3
- Fix xrandr revert behaviour (#119494)

* Tue Apr 13 2004 Warren Togami <wtogami@redhat.com> 1:2.6.0.3-2
- BR nautilus, eel2-devel, gettext
- remove missing macro from bonobo-activation-devel dep

* Fri Apr  2 2004 Alex Larsson <alexl@redhat.com> 1:2.6.0.3-1
- update to 2.6.0.3

* Thu Mar 18 2004 Warren Togami <wtogami@redhat.com> 2.5.4-2
- #109738 needs_terminal typo fixes, and set preferred browsers

* Thu Mar 11 2004 Mark McLoughlin <markmcredhat.com> 2.5.4-1
- Update to 2.5.4

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 27 2004 Jeremy Katz <katzj@redhat.com> - 1:2.5.3-2
- fix XKB stuff by adding the schema (#114477)
- add other missing schemas (#114526)

* Wed Feb 25 2004 Alexander Larsson <alexl@redhat.com> 1:2.5.3-1
- update to 2.5.3

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb  2 2004 Jonathan Blandford <jrb@redhat.com> 1:2.5.2-2
- temporary fix to get rid of error dialog.  Need to fix properly later

* Thu Jan 29 2004 Alexander Larsson <alexl@redhat.com> 1:2.5.2-2
- fix setting-daemon .server file

* Tue Jan 27 2004 Alexander Larsson <alexl@redhat.com> 1:2.5.2-1
- update to 2.5.2

* Wed Oct 29 2003 Jonathan Blandford <jrb@redhat.com> 1:2.4.0-3
- require libgail-gnome

* Mon Sep 22 2003 Jonathan Blandford <jrb@redhat.com> 1:2.4.0-2
- get all the schemas

* Mon Sep  8 2003 Jonathan Blandford <jrb@redhat.com>
- release 2.4.0

* Tue Aug 26 2003 Jonathan Blandford <jrb@redhat.com>
- Obsoletes: fontilus

* Mon Aug 25 2003 Jonathan Blandford <jrb@redhat.com> 1:2.3.5-1
- update to GNOME-2.4

* Thu Jun  5 2003 Jonathan Blandford <jrb@redhat.com> 1:2.2.2-1
- bump to new version

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May 27 2003 Alexander Larsson <alexl@redhat.com> 1:2.2.1-1
- Update to 2.2.1
- Add XRandR backport
- Remove patches already in, update cursorsupport patch to apply

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- debuginfo rebuild

* Thu Feb 20 2003 Jonathan Blandford <jrb@redhat.com> 1:2.2.0.1-8
- fixed cursorcapplet patch to not crash, #84485

* Tue Feb 18 2003 Jonathan Blandford <jrb@redhat.com> 1:2.2.0.1-7
- fix crasher, #84400

* Fri Feb 14 2003 Jeremy Katz <katzj@redhat.com> 1:2.2.0.1-6
- fix buildrequires

* Thu Feb  6 2003 Jonathan Blandford <jrb@redhat.com> 1:2.2.0.1-2
- add cursor support

* Thu Jan 30 2003 Jonathan Blandford <jrb@redhat.com>
- add patch to know which themes are supposed to be the default.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Jan 16 2003 Jonathan Blandford <jrb@redhat.com>
- bump version

* Wed Jan 15 2003 Jonathan Blandford <jrb@redhat.com>
- add "Go to fonts folder" button

* Mon Jan 13 2003 Jonathan Blandford <jrb@redhat.com>
- new version

* Mon Dec  2 2002 Havoc Pennington <hp@redhat.com>
- 2.1.3

* Wed Nov 13 2002 Havoc Pennington <hp@redhat.com>
- 2.1.2
- comment out the "fakingsucks" patch for esd
- remove most of the other patches
- remove patch to add WM/terminal font to font capplet, should be upstream
- comment out xftprefs patch for now

* Thu Sep  5 2002 Jonathan Blandford <jrb@redhat.com>
- Allow setting custom mime handlers

* Tue Aug 27 2002 Havoc Pennington <hp@redhat.com>
- make desktop file symlinks absolute #71991
- add po files from cvs.gnome.org

* Fri Aug 23 2002 Jonathan Blandford <jrb@redhat.com>
- Fix up keyboard handling

* Wed Aug 21 2002 Jonathan Blandford <jrb@redhat.com>
- Fixes for #68735

* Wed Aug  7 2002 Jonathan Blandford <jrb@redhat.com>
- New version.  Fix up metacity theme locations

* Wed Jul 24 2002 Owen Taylor <otaylor@redhat.com>
- Switch the gtk1 theme along with the gtk2 theme
- Add the ability to switch the window manager theme through the theme capplet
- Add two more font options to the font property dialog
- Add a bunch of missing unrefs of the result of gconf_client_get_default()

* Tue Jul 23 2002 Havoc Pennington <hp@redhat.com>
- fix desktop files more
- copy icons to /usr/share/pixmaps

* Tue Jul 23 2002 Havoc Pennington <hp@redhat.com>
- munge the desktop files correctly
- obsolete control-center-devel, #69168
- replace gnomecc.desktop with a file from redhat-menus

* Tue Jul 23 2002 Owen Taylor <otaylor@redhat.com>
- Fix crasher bug in xftprefs patch

* Tue Jul 16 2002 Owen Taylor <otaylor@redhat.com>
- Change the default rendering style to be "Best Shapes", not "Best Contrast"

* Tue Jul  9 2002 Owen Taylor <otaylor@redhat.com>
- Add Xft / XSETTINGS support

* Fri Jun 28 2002 Bill Nottingham <notting@redhat.com> 2.0.0-2
- fix %%post so schemas get installed
  
* Mon Jun 24 2002 Havoc Pennington <hp@redhat.com>
- 2.0.0
- add new default editor schemas
- fix find_lang

* Mon Jun 17 2002 Havoc Pennington <hp@redhat.com>
- rebuild for new libraries
- remove a no-longer-existing schemas file from post
- use desktop-file-install

* Fri Jun 07 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Wed Jun  5 2002 Havoc Pennington <hp@redhat.com>
- rebuild with new dependent libs

* Tue May 21 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Tue May 21 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment
- build requires bonobo-activation

* Tue May 21 2002 Havoc Pennington <hp@redhat.com>
- 1.99.10

* Fri May  3 2002 Havoc Pennington <hp@redhat.com>
- 1.99.9

* Wed Apr 17 2002 Havoc Pennington <hp@redhat.com>
- Move to GNOME 2 version

* Mon Apr 15 2002 Havoc Pennington <hp@redhat.com>
- merge in translations

* Fri Apr 12 2002 Owen Taylor <otaylor@redhat.com>
- Make the theme selector write fontsets, not fonts (#62413)

* Mon Apr  1 2002 Havoc Pennington <hp@redhat.com>
- really put screensaver capplet back (I think)

* Wed Mar 27 2002 Bill Nottingham <notting@redhat.com>
- revert xscreensaver change

* Wed Mar 27 2002 Havoc Pennington <hp@redhat.com>
- init "Scaled" radio button correctly #61913

* Mon Mar 25 2002 Havoc Pennington <hp@redhat.com>
- change path to windowmaker config tool again, #61824

* Thu Mar 14 2002 Bill Nottingham <notting@redhat.com>
- rather than keep patching and patching it, use xscreensaver's own
  capplet

* Wed Feb 27 2002 Havoc Pennington <hp@redhat.com>
- rebuild in Hampton

* Wed Jan 30 2002 Jonathan Blandford <jrb@redhat.com>
- Rebuild package.

* Thu Jan 24 2002 Tim Powers <timp@redhat.com>
- rebuilt against new openssl

* Fri Jan 18 2002 Havoc Pennington <hp@redhat.com>
- automake14
- don't run auto* again in ccsingle subdir, not sure why we did that

* Sun Oct 28 2001 Havoc Pennington <hp@redhat.com>
- rebuild with new gnome-libs so that libcapplet has right cflags/libs
- pixbufflags patch to make the rebuild work
- compileflags patch to make control-center-single work

* Wed Aug 29 2001 Havoc Pennington <hp@redhat.com>
- fix #52831 (UI properties in Programs menu)

* Mon Aug 27 2001 Havoc Pennington <hp@redhat.com>
- Add po files from sources.redhat.com

* Thu Aug 23 2001 Havoc Pennington <hp@redhat.com>
- set the _XROOTCOLOR_PIXEL property, should fix
  bug #52141

* Wed Aug 22 2001 Yukihiro Nakai <ynakai@redhat.com>
- Update translation.
- Add CJK fontset patch

* Thu Aug 16 2001 Jonathan Blandford <jrb@redhat.com>
- New control-center-single to handle exiting, #51665

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


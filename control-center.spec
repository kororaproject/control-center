%define gettext_package gnome-control-center-2.0

%define glib2_version 2.13.0
%define gtk2_version 2.11.6
%define gconf2_version 1.2.0
%define gnome_desktop_version 2.23.90
%define libgnome_version 2.3.0
%define libbonobo_version 2.3.0
%define libgnomeui_version 2.3.0
%define libbonoboui_version 2.3.0
%define gnome_vfs2_version 2.3.0
%define desktop_file_utils_version 0.9
%define xft_version 2.1.7
%define fontconfig_version 1.0.0
%define redhat_menus_version 1.8
%define metacity_version 2.23.1
%define libxklavier_version 3.6
%define gnome_menus_version 2.11.1
%define usermode_version 1.83
%define libgnomekbd_version 2.21

Summary: Utilities to configure the GNOME desktop
Name: control-center
Version: 2.25.2
Release: 5%{?dist}
Epoch: 1
License: GPLv2+ and GFDL
Group: User Interface/Desktops
Source: http://download.gnome.org/sources/gnome-control-center/2.25/gnome-control-center-%{version}.tar.bz2
Source1: org.gnome.control-center.defaultbackground.policy

# http://bugzilla.gnome.org/show_bug.cgi?id=562504
Patch1: gcc-enroll-stages.patch

Patch3: control-center-2.19.3-no-gnome-common.patch
# http://bugzilla.gnome.org/536531
Patch7: make-default.patch
# minor build breakage in gtk, will be fixed in the next gtk release
Patch8: gtkmarshal.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=466342
Patch10: gcc-sound-props-remove-oss.patch

# http://bugzilla.gnome.org/show_bug.cgi?id=545075 
Patch22: slab-icon-names.patch

# http://bugzilla.gnome.org/show_bug.cgi?id=554507
Patch25: ta-schema.patch

# http://bugzilla.gnome.org/show_bug.cgi?id=555591
Patch30: default-layout-toggle.patch

Patch32: display-no-help.patch

# call the Fedora/RHEL graphical passwd changing apps
Patch95: gnome-control-center-2.25.2-passwd.patch
Patch96: gnome-control-center-2.25.2-gecos.patch
# change default preferred apps to programs we ship
Patch99: default-applications.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 
URL: http://www.gnome.org

Obsoletes: gnome fontilus
# the background capplets expects its .xml files in 
# a different place now
Conflicts: desktop-backgrounds-basic < 2.0-27
Conflicts: desktop-backgrounds-extended < 2.0-27

Requires: gnome-settings-daemon >= 2.21.91-3
Requires: redhat-menus >= %{redhat_menus_version}
Requires: gnome-icon-theme
Requires: libgail-gnome
Requires: alsa-lib
Requires: gnome-menus >= %{gnome_menus_version}
Requires: usermode >= %{usermode_version}
Requires: gnome-desktop >= %{gnome_desktop_version}
Requires: dbus-x11
Requires: control-center-filesystem = %{epoch}:%{version}-%{release}
# for /usr/share/pkgconfig
Requires: pkgconfig

BuildRequires: autoconf automake libtool
BuildRequires: pango-devel 
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: librsvg2-devel
BuildRequires: GConf2-devel >= %{gconf2_version}
BuildRequires: gnome-desktop-devel >= %{gnome_desktop_version}
BuildRequires: libgnomeui-devel >= %{libgnomeui_version}
BuildRequires: libgnome-devel >= %{libgnome_version}
BuildRequires: libbonobo-devel >= %{libbonobo_version}
BuildRequires: libbonoboui-devel >= %{libbonoboui_version}
BuildRequires: gnome-vfs2-devel >= %{gnome_vfs2_version}
BuildRequires: fontconfig-devel >= %{fontconfig_version}
BuildRequires: desktop-file-utils >= %{desktop_file_utils_version}
BuildRequires: metacity-devel >= %{metacity_version}
BuildRequires: libxklavier-devel >= %{libxklavier_version}
BuildRequires: libXcursor-devel
BuildRequires: alsa-lib-devel
BuildRequires: nautilus-devel
BuildRequires: eel2-devel
BuildRequires: gettext
BuildRequires: gnome-menus-devel >= %{gnome_menus_version}
BuildRequires: gnome-panel-devel
BuildRequires: libgnomekbd-devel >= %{libgnomekbd_version}
BuildRequires: gnome-settings-daemon-devel
# For intltool:
BuildRequires: intltool >= 0.37.1
BuildRequires: perl(XML::Parser) 
BuildRequires: evolution-data-server-devel >= 1.9.1
BuildRequires: libXxf86misc-devel 
BuildRequires: libxkbfile-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: gnome-doc-utils
BuildRequires: gstreamer-devel
BuildRequires: gstreamer-plugins-base-devel
BuildRequires: libglade2-devel
BuildRequires: libxml2-devel
BuildRequires: hal-devel >= 0.5.6
BuildRequires: dbus-devel >= 0.90
BuildRequires: dbus-glib-devel >= 0.70
BuildRequires: scrollkeeper
BuildRequires: PolicyKit-gnome-devel
BuildRequires: libcanberra-devel

Requires(preun): GConf2
Requires(pre): GConf2
Requires(post): GConf2
Requires(post): desktop-file-utils >= %{desktop_file_utils_version}
Requires(post): shared-mime-info
Requires(postun): desktop-file-utils >= %{desktop_file_utils_version}
Requires(postun): shared-mime-info

%description
This package contains configuration utilities for the GNOME desktop, which
allow to configure accessibility options, desktop fonts, keyboard and mouse 
properties, sound setup, desktop theme and background, user interface 
properties, screen resolution, and other settings. 

%package devel
Summary: Development files for the GNOME control-center
Group: Development/Libraries
Requires: %{name} = %{?epoch}:%{version}-%{release}
Requires: pkgconfig

%description devel
Th control-center package contains configuration utilities for the 
GNOME desktop.

This package contains libraries and header files needed for integrating
configuration of applications such as window managers with the control-center
utilities.

%package filesystem
Summary: GNOME Control Center directories
Group: Development/Libraries
# NOTE: this is an "inverse dep" subpackage. It gets pulled in
# NOTE: by the main package an MUST not depend on the main package

%description filesystem
The GNOME control-center provides a number of extension points
for applications. This package contains directories where applications 
can install configuration files that are picked up by the control-center
utilities.

%prep
%setup -q -n gnome-control-center-%{version}

pushd capplets/about-me
%patch1 -p0 -b .num-enroll-stages
popd
%patch3 -p1 -b .no-gnome-common
%patch8 -p1 -b .gtkmarshal
%patch10 -p0 -b .no-oss
%patch22 -p0 -b .slab-icon-names
%patch25 -p1 -b .ta-schema
%patch30 -p1 -b .default-layout-toggle
%patch32 -p1 -b .display-no-help

# vendor configuration patches
%patch95 -p1 -b .passwd
%patch96 -p1 -b .gecos
%patch99 -p1 -b .default-apps

%patch7 -p1 -b .make-default

autoreconf -f -i

%build

# Work-around http://bugzilla.gnome.org/show_bug.cgi?id=427939
sed -i -e 's/@ENABLE_SK_TRUE@_s/_s/' help/Makefile.in

# Add -Wno-error to silence gswitchit
%configure --disable-static \
	--disable-scrollkeeper \
	--enable-gstreamer \
	--enable-alsa \
	--enable-aboutme \
	--disable-update-mimedb \
	CFLAGS="$RPM_OPT_FLAGS -Wno-error" 
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

for i in apps_gnome_settings_daemon_default_editor.schemas		\
	    apps_gnome_settings_daemon_keybindings.schemas		\
	    apps_gnome_settings_daemon_screensaver.schemas		\
	    desktop_gnome_font_rendering.schemas ; do			\
	    rm -f $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas/$i ;	\
done

# Add a "valid" OnlyShowIn entry, otherwise desktop-file-install complains
sed -i -e "s/OnlyShowIn=;/OnlyShowIn=GNOME;/"  \
  $RPM_BUILD_ROOT%{_datadir}/applications/gnome-theme-installer.desktop

desktop-file-install --vendor gnome --delete-original			\
  --dir $RPM_BUILD_ROOT%{_datadir}/applications				\
  --add-only-show-in GNOME						\
  $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

sed -i -e "s/OnlyShowIn=GNOME;/OnlyShowIn=;/"  \
  $RPM_BUILD_ROOT%{_datadir}/applications/gnome-theme-installer.desktop

# https://bugzilla.redhat.com/show_bug.cgi?id=161489
sed -i -e "s/OnlyShowIn=GNOME;//"  \
  $RPM_BUILD_ROOT%{_datadir}/applications/gnome-default-applications.desktop

# we do want this
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties

mkdir -p $RPM_BUILD_ROOT%{_datadir}/PolicyKit/policy
install -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/PolicyKit/policy

# we don't want these
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnome/autostart
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnome/cursor-fonts

rm $RPM_BUILD_ROOT%{_datadir}/applications/mimeinfo.cache

# remove useless libtool archive files
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} \;

%find_lang %{gettext_package} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule 		       \
   %{_sysconfdir}/gconf/schemas/control-center.schemas \
   %{_sysconfdir}/gconf/schemas/fontilus.schemas \
     > /dev/null || :
update-desktop-database --quiet %{_datadir}/applications
update-mime-database %{_datadir}/mime > /dev/null
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    for f in fontilus.schemas control-center.schemas; do
        if [ -f %{_sysconfdir}/gconf/schemas/$f ]; then
            gconftool-2 --makefile-uninstall-rule \
		%{_sysconfdir}/gconf/schemas/$f \
                > /dev/null || :
        fi
    done
fi

%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    for f in fontilus.schemas control-center.schemas; do
        if [ -f %{_sysconfdir}/gconf/schemas/$f ]; then
            gconftool-2 --makefile-uninstall-rule \
		%{_sysconfdir}/gconf/schemas/$f \
                > /dev/null || :
        fi
    done
fi

%postun
/sbin/ldconfig
update-desktop-database --quiet %{_datadir}/applications
update-mime-database %{_datadir}/mime > /dev/null
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%files -f %{gettext_package}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README
%{_datadir}/gnome-control-center/keybindings/*.xml
%{_datadir}/gnome-control-center/default-apps/*.xml
%{_datadir}/gnome-control-center/glade
%{_datadir}/gnome-control-center/pixmaps
%{_datadir}/applications/*.desktop
%{_datadir}/desktop-directories/*
%{_datadir}/mime/packages/gnome-theme-package.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/PolicyKit/policy/*
%{_datadir}/pkgconfig/gnome-keybindings.pc
%{_datadir}/pkgconfig/gnome-default-applications.pc
# list all binaries explicitly, so we notice if one goes missing
%{_bindir}/gnome-about-me
%{_bindir}/gnome-appearance-properties
%{_bindir}/gnome-at-mobility
%{_bindir}/gnome-at-properties
%{_bindir}/gnome-at-visual
%{_bindir}/gnome-control-center
%{_bindir}/gnome-default-applications-properties
%{_bindir}/gnome-display-properties
%{_bindir}/gnome-keybinding-properties
%{_bindir}/gnome-keyboard-properties
%{_bindir}/gnome-mouse-properties
%{_bindir}/gnome-network-preferences
%{_bindir}/gnome-sound-properties
%{_bindir}/gnome-typing-monitor
%{_bindir}/gnome-window-properties
%{_bindir}/gnome-font-viewer
%{_bindir}/gnome-thumbnail-font
%{_libdir}/*.so.*
%{_sysconfdir}/gconf/schemas/control-center.schemas
%{_sysconfdir}/gconf/schemas/fontilus.schemas
%{_sysconfdir}/xdg/menus/gnomecc.menu
%{_sysconfdir}/xdg/autostart/gnome-at-session.desktop
%{_libdir}/window-manager-settings/*.so

%files devel
%defattr(-,root,root)
%{_includedir}/gnome-window-settings-2.0
%{_libdir}/libgnome-window-settings.so
%{_libdir}/pkgconfig/*

%files filesystem
%defattr(-,root,root)
%dir %{_libdir}/window-manager-settings
%dir %{_datadir}/gnome/wm-properties
%dir %{_datadir}/gnome-control-center
%dir %{_datadir}/gnome-control-center/keybindings

%changelog
* Mon Dec 08 2008 - Bastien Nocera <bnocera@redhat.com> - 2.25.2-5
- Add patch to support multiple enrollment stages in the about-me
  capplet

* Thu Dec  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.2-4
- Update to 2.25.2

* Thu Nov 21 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.1-6
- Tweak %%summary and %%description

* Thu Nov 13 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.1-5
- Update to 2.25.1

* Thu Nov  6 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0.1-9
- Remove a nonworking help button (#470375)

* Sun Oct 19 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0.1-8
- Fix a ui glitch in the keybinding capplet

* Fri Oct 10 2008 - Bastien Nocera <bnocera@redhat.com> - 2.24.0.1-7
- Remove OSS from the possible options (#466342)

* Fri Oct 10 2008 - Bastien Nocera <bnocera@redhat.com> - 2.24.0.1-6
- When a sound is selected with the file chooser in g-s-p, make
  sure to default to /usr/share/sounds if that dir exists
  (#456919)

* Wed Oct  8 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0.1-5
- Change the default key combination to change keyboard layouts
  to shift-capslock, since alt-alt doesn't work (#465403)

* Sat Oct  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0.1-4
- Fix horizontal/vertical maximization preference

* Sat Oct  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0.1-3
- Fix help buttons in the appearance capplet

* Tue Sep 30 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0.1-2
- Fix a schema mistranslation

* Wed Sep 24 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0.1-1
- Update to 2.24.0.1

* Tue Sep 23 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Fri Aug 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.90-1
- Update to 2.23.90

* Tue Aug  5 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.6-1
- Update to 2.23.6

* Thu Jul 31 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.5-8
- Yet more icon fixes

* Mon Jul 28 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.5-7
- Fix the icon name patch

* Mon Jul 28 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.5-6
- Use standard icon names in more places

* Sun Jul 27 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.5-5
- Fix up gconf schema installation

* Sat Jul 26 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.5-4
- Use standard icon names in more places

* Fri Jul 25 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.5-3
- Remove testing hack

* Thu Jul 24 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.5-2
- Update the libcanberra patch

* Thu Jul 24 2008 Soren Sandmann <sandmann@redhat.com> - 2.23.5-1
- Update the packaged files to match reality.

* Thu Jul 24 2008 Soren Sandmann <sandmann@redhat.com> - 2.23.5-1
- Update to 2.23.5. Drop randr, standard icon and
  notification theme patches. 
- Comment out libcanberra patch for now since it doesn't apply

* Thu Jul 24 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.4-6
- Add patch to support the Free Desktop sound theme spec
- Remove gnome-vfs-methods as per upstream

* Thu Jul 24 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.4-5
- Remove some obsolete patches

* Mon Jul 14 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.4-4
- Drop some obsolete patches
- Fix an issue with the notification-theme support (#455329)

* Mon Jun 23 2008 Ray Strode <rstrode@redhat.com> - 2.23.4-3
- Install bg capplet .policy file

* Fri Jun 20 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.4-2
- Use standard icon names for capplets where available

* Wed Jun 18 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.4-1
- Update to 2.23.4

* Wed Jun  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.3-1
- Update to 2.23.3

* Tue Jun  3 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.2-2
- Make changing default backgrounds work better

* Tue May 27 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.2-1
- Update to 2.23.2

* Sat May 17 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.1-4
- Support notication themes in the appearance capplet

* Tue May 13 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.1-3
- Rebuild against newer libs

* Fri May  2 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.1-2
- Add a button to change the default background

* Fri Apr 25 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.1-1
- Update to 2.23.1

* Tue Apr  8 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.1-2
- Remove a nonfunctional button from the a11y preferences

* Tue Apr 08 2008 - Bastien Nocera <bnocera@redhat.com> - 2.22.1-1
- Update to 2.22.1

* Mon Apr 7 2008 Soren Sandmann <sandmann@redhat.com> - 2.22.0-7
- Add window title, improve wording in label

* Mon Apr 7 2008 Soren Sandmann <sandmann@redhat.com> - 2.22.0-6
- Disallow turning off the only active screen

* Mon Apr 7 2008 Soren Sandmann <sandmann@redhat.com> - 2.22.0-5
- Add detect displays button; fix clone text

* Thu Apr 5 2008 Soren Sandmann <sandmann@redhat.com> - 2.22.0-4
- Better clone mode support. Remove debug text.

* Mon Mar 31 2008 - Bastien Nocera <bnocera@redhat.com> - 2.22.0-3
- Fix warnings in the keybindings capplet when in non-UTF-8 locale
- Fix Esc/Backspace being bindable when CapsLock is on (#427123)

* Thu Mar 20 2008 Soren Sandmann <sandmann@redhat.com> - 2.22.0-2
- Update randr

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.0-1
- Update to 2.22.0

* Sun Mar  2 2008 Soren Sandmann <sandmann@redhat.com> - 2.21.92-3
- Update randr

* Fri Feb 29 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.92-2
- Fix broken schema translations

* Tue Feb 26 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.92-1
- Update to 2.21.92

* Wed Feb 13 2008 Soren Sandmann <sandmann@redhat.com> - 2.21.90-10
- Update randr capplet

* Wed Feb 13 2008 Soren Sandmann <sandmann@redhat.com> - 2.21.90-9
- Update randr capplet

* Tue Feb 12 2008 Soren Sandmann <sandmann@redhat.com> - 2.21.90-8
- Update randr capplet

* Mon Feb 4 2008 Soren Sandmann <sandmann@redhat.com> - 2.21.90-7
- Update randr capplet

* Mon Feb 4 2008 Soren Sandmann <sandmann@redhat.com> - 2.21.90-6
- Update randr capplet - now with rotation

* Thu Jan 29 2008 Soren Sandmann <sandmann@redhat.com> - 2.21.90-5
- Update randr capplet

* Thu Jan 29 2008 Soren Sandmann <sandmann@redhat.com> - 2.21.90-4
- Update randr capplet

* Thu Jan 29 2008 Soren Sandmann <sandmann@redhat.com> - 2.21.90-3
- Update randr capplet

* Tue Jan 29 2008 Soren Sandmann <sandmann@redhat.com> - 2.21.90-2
- Various updates to randr applet

* Tue Jan 29 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.90
- Update to 2.21.90
- Update RandR applet patch to apply

* Tue Jan 29 2008 Soren Sandmann <sandmann@redhat.com> - 2.21.5-4
- BuildRequire gnome-desktop 2.21.90 

* Tue Jan 29 2008 Soren Sandmann <sandmann@redhat.com> - 2.21.5-3
- Add new randr 1.2 capplet

* Tue Jan 22 2008  Matthias Clasen <mclasen@redhat.com> - 2.21.5-2
- Disable font folder support

* Thu Jan 17 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.5-1
- Update to 2.21.5

* Fri Jan 11 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.4-3
- Remove duplicated sylpheed entry (#428363)

* Mon Dec 24 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.4-2
- Rebuild nautilus extensions against new nautilus

* Fri Dec 21 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.4-1
- Update to 2.21.4

* Tue Dec 18 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.2-3
- Support the gtk-im-module setting

* Sun Nov 18 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.2-2
- Spec file cleanups

* Tue Nov 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.2-1
- Update to 2.21.2

* Tue Oct 30 2007 - Bastien Nocera <bnocera@redhat.com> - 2.20.1-7
- Remove useless "start esd" preference

* Wed Oct 24 2007  Matthias Clasen <mclasen@redhat.com> - 2.20.1-6
- Fix the orca command in the default applications capplet (#351471)
 
* Tue Oct 23 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.1-5
- Rebuild against new dbus-glib

* Fri Oct 19 2007 - Ray Strode <rstrode@redhat.com> - 2.20.1-4
- Update libxklavier buildreq (bug 339731)

* Thu Oct 18 2007 - Bastien Nocera <bnocera@redhat.com> - 2.20.1-3
- Bind more default keys in the keybindings capplet (#330501)

* Thu Oct 18 2007 - Bastien Nocera <bnocera@redhat.com> - 2.20.1-2
- Remove OnlyShowIn GNOME from the default apps, so that KDE users
  can change their mailto: handlers easily (#161489)

* Mon Oct 15 2007 - Bastien Nocera <bnocera@redhat.com> - 2.20.1-1
- Update to 2.20.1

* Tue Oct 09 2007 - Bastien Nocera <bnocera@redhat.com> - 2.20.0.1-2
- Add patch to make XF86* keysyms the default for audio keybindings,
  so that we work out-of-the-box when the rights keymap is selected
  (#324931)
- Fix build

* Wed Sep 26 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0.1-1
- Update to 2.20.0.1 (small bug fixes)

* Mon Sep 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-1
- Update to 2.20.0

* Tue Sep  4 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.92-1
- Update to 2.19.92

* Thu Aug 30 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.91.-1
- Update to 2.19.91
- Update the background and the default-apps patches

* Mon Aug 20 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.90-4
- Kill some shell warnings (#239439)
- Remove outdated, unapplied patches

* Fri Aug 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.90-3
- Improve tooltips for slide shows

* Thu Aug 16 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.90-2
- Port Soerens background patch to the appearance capplet

* Mon Aug 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.90-1
- Update to 2.19.90
- Build the sound capplet again

* Mon Aug  6 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.6-3
- Update the license field again
- Use %%find_lang for help files, too

* Fri Aug  3 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.6-2
- Update the license field

* Mon Jul 30 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.6-1
- Update to 2.19.6

* Wed Jul 25 2007 Jesse Keating <jkeating@redhat.com> - 2.19.5-4
- Rebuild for RH #249435

* Mon Jul 23 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.5-3
- Port to new GTK+ tooltips API

* Thu Jul 12 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.5-2
- Tiny improvement to the default applications capplet

* Tue Jul 10 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.5-1 
- Update to 2.19.5

* Wed Jun 27 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.4-7
- Don't ship old unused cursor fonts 

* Wed Jun 27 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.4-6
- Remove some questionable a11y autostart files, too
- Add a filesystem subpackage

* Wed Jun 27 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.4-5
- Remove some questionable a11y menu items

* Thu Jun 21 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.4-4
- Fix starting of screensavers

* Tue Jun 19 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.4-3
- Fix a segfault in the background-setting code

* Tue Jun 19 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.4-2
- Fix up the new module handling in gnome-settings-daemon

* Mon Jun 18 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.4-1
- Update to 2.19.4

* Wed Jun 06 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.3-6
- Remove gst-inspect call, as the configure doesn't check for
  specific plugins

* Tue Jun  5 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.3-5
- Another rebuild, fixing some Makefile syntax problems

* Tue Jun 05 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.3-4
- Another rebuild with GStreamer for PPC rebuilt

* Tue Jun 05 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.3-3
- And update for added files

* Tue Jun 05 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.3-2
- Update for removed files

* Tue Jun  5 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.3-1
- Update to 2.19.3

* Tue May 22 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.1-8
- And go to the right directory to apply patch17

* Tue May 22 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.1-7
- Really apply the patch for ~/.face permissions

* Tue May 22 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.1-6
- Fix the datadir control-center being renamed to gnome-control-center
- Don't package slab devel files, we don't install them anymore

* Tue May 22 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.1-5
- Fix the gettext_package, as control-center changed its name

* Tue May 22 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.1-4
- Add a hack to avoid desktop-file-install complaining about missing
  desktop name in OnlyShownIn

* Mon May 21 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.1-3
- Remove the compiz support patch, compiz should ship it's keybindings XML
  file itself
- Remove libxslt BR as it should be pulled by scrollkeeper
- Add a work-around for GNOME bug 427939

* Mon May 21 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.1-2
- Add libxslt as a BR so that xsltproc can be used to generate the .omf files

* Sat May 10 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.1-1
- Update to 2.19.1

* Tue May 01 2007 - Bastien Nocera <bnocera@redhat.com> - 2.18.0-16
- Add missing dbus-x11 dependency, otherwise gnome-settings-daemon
  cannot be started (#204706)

* Tue May 01 2007 - Bastien Nocera <bnocera@redhat.com> - 2.18.0-15
- Add a patch to set the permissions on ~/.face so that GDM can
  show them (#236393)

* Wed Apr 18 2007 Soren Sandmann <sandmann@redhat.com> - 2.18.0-14
- Add control-center-2.18.0-gnome-bg.patch contents. Apply it again

* Tue Apr 17 2007 Ray Strode <rstrode@redhat.com> - 2.18.0-13
- clean up be-more-async patch to have less repetitive code 

* Tue Apr 17 2007 Ray Strode <rstrode@redhat.com> - 2.18.0-12
- Make theme changes work again (among other things). 
  Bug 236752. 

* Tue Apr 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-11
- Remove debugging spew from the about-me capplet

* Mon Apr 16 2007 Ray Strode <rstrode@redhat.com> - 2.18.0-10
- Remove trailing space after escaped newline in schema post
  install.  Reported by Yanko Kaneti.

* Fri Apr 13 2007 Ray Strode <rstrode@redhat.com> - 2.18.0-9
- Load settings-daemon parts more asynchronously (to help with
  bug 236296)

* Thu Apr 12 2007 David Zeuthen <davidz@redhat.com> - 2.18.0-8
- Disable start-at-helper patch for now (#223669)
- Disable gnome-bg patch as it's empty
- BR metacity-devel

* Tue Apr  3 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-7
- Fix a problem with the previous patch

* Mon Apr  2 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-6
- Ellipsize sound devices in the sound capplet

* Fri Mar 23 2007 Soren Sandmann <sandmann@redhat.com> - 2.18.0-5
- Remove debug spew from gnome-bg patch

* Wed Mar 21 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-4
- Try hard to not show the theme installer

* Mon Mar 19 2007 Soren Sandmann <sandmann@redhat.com> - 2.18.0-3
- Add control-center-2.18.0-gnome-bg.patch to support time changing
  backgrounds in gnome-settings-daemon and gnome-wp-capplet

* Mon Mar 19 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-2
- Don't show the theme installer in the menus

* Tue Mar 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-1
- Update to 2.18.0

* Wed Feb 28 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.92-1
- Update to 2.17.92
- Drop obsolete patches

* Wed Feb 14 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.91-2
- Fix scriptlets

* Tue Feb 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.91-1
- Update to 2.17.91
- Drop upstreamed patches
- Update patches

* Wed Feb  7 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.90-6
- Make gstreamer pulse plugin show up in the sound capplet

* Tue Feb  6 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.90-5
- Fix some problems with the color theme support

* Mon Feb  5 2007 Ray Strode <rstrode@redhat.com> - 2.17.90-4
- remove crufty sed replace line
- use find -name '*.la' instead of removing each one
  individually

* Mon Jan 29 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.90-3
- Support tracker in the search keybinding (#216315)

* Tue Jan 23 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.90-2
- Install gnomecc desktop file

* Mon Jan 22 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.90-1
- Update to 2.17.90

* Thu Jan 11 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.5-1
- Update to 2.17.5

* Sat Dec  9 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.3-2
- Spec file cleanups

* Tue Dec  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.3-1
- Update to 2.17.3

* Sat Nov 18 2006 Ray Strode <rstrode@redhat.com> - 2.17.1-6
- update file list to explicitly mention schema files
- fix %%pre scriplet

* Fri Nov 17 2006 Ray Strode <rstrode@redhat.com> - 2.17.1-5
- apply aforementioned thumbnail fixups

* Fri Nov 17 2006 Ray Strode <rstrode@redhat.com> - 2.17.1-4
- Drop unused/bogus patches
- Try to fix up background capplet thumbnail code again (better this time)
- rearrange patches so that vendor patches end up at the end

* Wed Nov  8 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.1-3
- Work around a file conflict with libgnomekbd (#214608)

* Fri Oct 27 2006 Matthew Barnes <mbarnes@redhat.com> - 2.17.1-2.fc7
- Update BuildRequires for evolution-data-server-devel.
- Rebuild against evolution-data-server-1.9.1.

* Sat Oct 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.1-1
- Update to 2.17.1

* Tue Oct 10 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-10
- Don't show a nonworking help button in the about-me capplet (#201878)

* Fri Sep 29 2006 Christopher Aillon <caillon@redhat.com> - 2.16.0-9
- Don't let default-applications tell official gecko applications
  to launch new tabs or windows, as it causes them to not launch when 
  there is no running instance.

* Thu Sep 28 2006 Soren Sandmann <sandmann@redhat.com> - 2.16.0-8
- Update the compiz-support.patch to support raising of windows (and also
  show-desktop) (Bug 204129).

* Wed Sep 27 2006 Soren Sandmann <sandmann@redhat.com> - 2.16.0-7
- Update the compiz-support.patch to use the correct gconf keys for
  the compiz keyboard bindings. (Bug 204094).

* Tue Sep 26 2006 Soren Sandmann <sandmann@redhat.com> - 2.16.0-6
- Update the compiz-support patch to also make the "Desktop" keybindings
  work. Bug 200290.

* Tue Sep 19 2006 John (J5) Palmieri <johnp@redhat.com> - 2.16.0-5
- Update the Orca patch

* Tue Sep 19 2006 John (J5) Palmieri <johnp@redhat.com> - 2.16.0-4
- Add a patch to start/stop and configure Orca from the accessibilities
  capplet

* Wed Sep 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-3
- Correct the Thunderbird and Evolution commands in
  the list of default applications  (#197135)
 
* Mon Sep  4 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-2.fc6
- Update to 2.16.0

* Sun Aug 27 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.92-5.fc6
- Fix some redraw issues in the keyboard capplet

* Sun Aug 27 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.92-4.fc6
- More keyboard capplet improvements

* Thu Aug 24 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.92-3.fc6
- Various improvements for the keyboard capplet

* Thu Aug 24 2006 Ray Strode <rstrode@redhat.com> - 2.15.92-2.fc6
- don't try to map user defined key shortcuts to keysyms
  (bug 201176)

* Tue Aug 22 2006 Ray Strode <rstrode@redhat.com> - 2.15.92-1.fc6
- update to 2.15.92

* Tue Aug 22 2006 Soren Sandmann <sandmann@redhat.com> - 2.15.91-6.fc6
- Add support for compiz in keybinding dialog.

* Mon Aug 21 2006 Ray Strode <rstrode@redhat.com> - 2.15.91-5.fc6
- When creating new thumbnails, record thumbnail location rather
  that regenerating them over and over again.

* Fri Aug 18 2006 Ray Strode <rstrode@redhat.com> - 2.15.91-4.fc6
- Fix thumbnailing problem in background capplet (bug 185142)

* Mon Aug 14 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.91-3.fc6
- Make the search keybinding work with beagle

* Sun Aug 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.91-2.fc6
- fix spec file (pointed out by Yanko Kaneti)

* Sun Aug 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.91-1.fc6
- Update to 2.15.91

* Mon Aug 07 2006 Karsten Hopp <karsten@redhat.com> 2.15.90-4
- add fix for new libebook api

* Sun Aug 06 2006 Florian La Roche <laroche@redhat.com>
- rebuild for deps

* Fri Aug  4 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.90-1.fc6
- Update to 2.15.90

* Mon Jul 24 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.4-6
- Make gnome-about-me start 

* Sat Jul 22 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.4-5
- Fix the close button of the background capplet

* Wed Jul 19 2006 John (J5) Palmieri <johnp@redhat.com> - 2.15.4-4
- Add patch to use the dbus cflags and libs instead of relying on hal
  flags to populate them

* Tue Jul 18 2006 John (J5) Palmieri <johnp@redhat.com> - 2.15.4-3
- Add BR on dbus-glib-devel

* Thu Jul 13 2006 Ray Strode <rstrode@redhat.com> - 2.15.4-2
- go to latest background capplet

* Wed Jul 12 2006 Matthias Clasen  <mclasen@redhat.com> - 2.15.4-1
- Update to 2.15.4

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
/- rebuild with new dependent libs

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


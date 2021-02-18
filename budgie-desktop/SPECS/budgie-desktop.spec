%global debug_package %{nil}

Name:    budgie-desktop
Version: 10.5.2
Release: 6.mrx8
Packager: <akotov>
License: GPLv2 and LGPLv2.1
Summary: An elegant desktop with GNOME integration
URL:     https://github.com/solus-project/budgie-desktop

Source: budgie-desktop-%{version}.tar.gz

# [PATCH] Fix errors were caused by desktop-file-validate
Patch0: 2762bebcde92902c08bb25ac4ea5eef022ecd502.patch
# [PATCH] + Keyboard layout ['<Shift>Alt_L']
Patch1: shift-alt.patch

BuildRequires: peas-devel
BuildRequires: gnome-desktop-devel
BuildRequires: sassc
BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(vapigen)
BuildRequires: pkgconfig(ibus-1.0)
BuildRequires: pkgconfig(gnome-settings-daemon)
BuildRequires: pkgconfig(libwnck-3.0)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: libmutter-devel
BuildRequires: pkgconfig(libgnome-menu-3.0)
BuildRequires: pkgconfig(upower-glib)
BuildRequires: libgnomebt-devel

BuildRequires: vala
BuildRequires: ninja
BuildRequires: meson
BuildRequires: cmake
BuildRequires: intltool
BuildRequires: gtk-doc
BuildRequires: desktop-file-utils
#Для *.mrx8
BuildRequires: mesaegl-devel
BuildRequires: git
BuildRequires: locales-en

Requires: mutter
Requires: gtk+3.0
Requires: task-x11
Requires: dbus-x11
Requires: libwnck3
Requires: hicolor-icon-theme
Requires: gnome-session
Requires: gnome-bluetooth
#Requires: gnome-themes-extra
Requires: gnome-screensaver
Requires: typelib(Peas)
Requires: typelib(Graphene)
Requires: typelib(GMenu)
Requires: task-pulseaudio
#nemo-desktop not start after upgrade without xapps
Requires: xapps

#MgaRemix (nautilus -> nemo for desktop icons)
Recommends: nemo
Recommends: nemo-emblems
Recommends: nemo-fileroller
Recommends: file-roller
#Recommends: nemo-image-converter

#MgaRemix other Recommends packages
#Recommends: gnome-tweaks - тянет за собой gmome-shell, gdm и кучу ненужных либ
Recommends: dconf-editor
Recommends: gnome-disk-utility
Recommends: gnome-calculator
#Recommends: gnome-shell-extension-topicons
Recommends: gnome-screenshot
Recommends: gnome-terminal

Recommends: mc
Recommends: lightdm
#Recommends: networkmanager
#Recommends: pulseaudio

Recommends: xed
Recommends: mtools
Recommends: xrandr

# like task-kde4, but suggests instead of requires
Recommends: task-codec-audio
Recommends: task-codec-video

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

Requires: %{name}-libs
Requires: %{name}-plugins-core
Requires: %{name}-schemas
Requires: %{name}-rundialog

%description
Budgie is the flagship desktop of the Solus, and is an Solus project.
The Budgie Desktop a modern desktop designed to keep out the way of
the user. It features heavy integration with the GNOME stack in order
for an enhanced experience.

%package        plugins-core
Summary:        Core plugins for the Budgie Desktop
#MgaRemix
Requires:       gtk+3.0
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-schemas%{?_isa} = %{version}-%{release}

%description    plugins-core
This package contains the core plugins of Budgie Desktop.

%package        rundialog
Summary:        Budgie Run Dialog for the Budgie Desktop
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-schemas%{?_isa} = %{version}-%{release}

%description    rundialog
Budgie Run Dialog for the Budgie Desktop

%package        libs
Summary:        Common libs for the Budgie Desktop
#MgaRemix
Requires:       gtk+3.0

%description    libs
This package contains the shared library of Budgie Desktop.

%package        schemas
Summary:        GLib schemas for the Budgie Desktop

%description    schemas
GLib schemas for the Budgie Desktop

%package        docs
Summary:        GTK3 Desktop Environment -- Documentation files
Group:          Documentation/HTML

%description    docs
GTK3 Desktop Environment -- Documentation files.
This package provides API Documentation for the Budgie Plugin API, in the
GTK-Doc HTML format.

%package        devel
Summary:        Development files for the Budgie Desktop
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the files required for developing for Budgie Desktop.

%prep
%setup -q -T -b 0 -n %{name}-%{version}
%patch0 -p1
# Keyboard layout ['<Shift>Alt_L']
%patch1 -p1

%build
export LC_ALL=en_US.utf8

#MgaRemix (without desktop icons)
%meson --prefix=%{_prefix} --libdir=%{_libdir}

%meson_build

%install
export LC_ALL=en_US.utf8

%meson_install
find %{buildroot} -name '*.la' -delete

%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/budgie-*.desktop

#MgaRemix
%post
ldconfig
#Gnome menu link
if [ ! -f "/etc/xdg/menus/gnome-applications-menu" ]; then
    cd /etc/xdg/menus
    ln -s applications.menu gnome-applications.menu
fi;
#Nemo autostart
echo "[Desktop Entry]" > /etc/xdg/autostart/budgie-nemo-autostart.desktop
echo "Type=Application" >> /etc/xdg/autostart/budgie-nemo-autostart.desktop
echo "Name=Nemo" >> /etc/xdg/autostart/budgie-nemo-autostart.desktop
echo "Comment=Start Nemo desktop at log in" >> /etc/xdg/autostart/budgie-nemo-autostart.desktop
echo "Exec=nemo-desktop" >> /etc/xdg/autostart/budgie-nemo-autostart.desktop
echo "OnlyShowIn=X-Budgie;" >> /etc/xdg/autostart/budgie-nemo-autostart.desktop
echo "AutostartCondition=GSettings org.nemo.desktop show-desktop-icons" >> /etc/xdg/autostart/budgie-nemo-autostart.desktop
echo "X-GNOME-AutoRestart=true" >> /etc/xdg/autostart/budgie-nemo-autostart.desktop
echo "NoDisplay=true" >> /etc/xdg/autostart/budgie-nemo-autostart.desktop
echo "Name[ru_RU]=budgie-nemo-autostart.desktop" >> /etc/xdg/autostart/budgie-nemo-autostart.desktop

%files -f %{name}.lang
%doc README.md
%license LICENSE LICENSE.LGPL2.1
%{_bindir}/budgie-*
%config(noreplace) %{_sysconfdir}/xdg/autostart/budgie-desktop-*.desktop
%{_datadir}/applications/budgie-*.desktop
%{_datadir}/gnome-session/sessions/budgie-desktop.session
%{_datadir}/icons/hicolor/scalable/apps/budgie-desktop-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/notification-alert-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/pane-hide-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/pane-show-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/system-hibernate-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/system-log-out-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/system-restart-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/system-suspend-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/clock-applet-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/icon-task-list-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/notifications-applet-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/notification-disabled-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/separator-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/spacer-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/system-tray-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/task-list-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/workspace-switcher-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/my-caffeine-on-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/budgie-caffeine-cup-empty.svg
%{_datadir}/icons/hicolor/scalable/status/budgie-caffeine-cup-full.svg
%{_datadir}/icons/hicolor/scalable/status/caps-lock-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/num-lock-symbolic.svg
%{_datadir}/xsessions/budgie-desktop.desktop

%files plugins-core
%{_libdir}/budgie-desktop/*

%files schemas
%{_datadir}/glib-2.0/schemas/com.solus-project.*.gschema.xml
%{_datadir}/glib-2.0/schemas/20_solus-project.budgie.wm.gschema.override

%files libs
%{_libdir}/budgie-desktop/
%{_libdir}/libbudgietheme.so.0
%{_libdir}/libbudgietheme.so.0.0.0
%{_libdir}/libbudgie-plugin.so.0
%{_libdir}/libbudgie-plugin.so.0.0.0
%{_libdir}/libbudgie-private.so.0
%{_libdir}/libbudgie-private.so.0.0.0
%{_libdir}/libraven.so.0
%{_libdir}/libraven.so.0.0.0
%{_libdir}/girepository-1.0/Budgie*.typelib

%files rundialog
%{_bindir}/budgie-run-dialog

%files docs
%{_datadir}/gtk-doc/html/budgie-desktop/

%files devel
%{_includedir}/budgie-desktop/
%{_libdir}/pkgconfig/budgie*.pc
%{_libdir}/libbudgietheme.so
%{_libdir}/libbudgie-plugin.so
%{_libdir}/libbudgie-private.so
%{_libdir}/libraven.so
%{_datadir}/gir-1.0/Budgie-1.0.gir
%{_datadir}/vala/vapi/budgie-1.0.*

%changelog
* Mon Sep 09 2019 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20190909.67769ea-1
- build from commit 67769ea09299e57f3a4ceeb2223f642d86ecafcf
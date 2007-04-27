%define name gedit-root
%define version 1.0
%define release %mkrel 2
Summary: Lets you launch gedit as root from the menu
Source0: gedit-root.console
Source1: gedit-root.desktop
License: GPL
Group: Editors
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: gedit
Requires: usermode-consoleonly
Name: %{name}
Version: %{version}
Release: %{release}

%description
%{name} creates a command named %{name} which launches gedit with
root privileges (after authenticating via consolehelper), and adds a
menu launcher so you can launch gedit as root from the system menu.

%install
rm -rf $RPM_BUILD_ROOT
test -z $RPM_BUILD_ROOT%{_sysconfdir}/security/console.apps || mkdir -p -- . "$RPM_BUILD_ROOT%{_sysconfdir}/security/console.apps"
install -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/security/console.apps/gedit-root
test -z $RPM_BUILD_ROOT%{_datadir}/applications || mkdir -p -- . "$RPM_BUILD_ROOT%{_datadir}/applications"
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/gedit-root.desktop
test -z $RPM_BUILD_ROOT%{_bindir} || mkdir -p -- . "$RPM_BUILD_ROOT%{_bindir}"
ln -s %{_bindir}/consolehelper $RPM_BUILD_ROOT%{_bindir}/gedit-root

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_desktop_database}
%{update_menus}

%postun
%{clean_menus}
%{clean_desktop_database}

%files
%defattr(-, root, root)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_sysconfdir}/security/console.apps/%{name}

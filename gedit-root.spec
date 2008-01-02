Name:		gedit-root
Summary:	Lets you launch gedit as root from the menu
Version:	1.0
Release:	%mkrel 3
Source0:	gedit-root.console
Source1:	gedit-root.desktop
Source2:	gedit-root.pam
License:	GPLv2+
Group:		Editors
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	gedit
Requires:	usermode-consoleonly

%description
%{name} creates a command named %{name} which launches gedit with
root privileges (after authenticating via consolehelper), and adds a
menu launcher so you can launch gedit as root from the system menu.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/security/console.apps
install -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/security/console.apps/%{name}
mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pam.d/%{name}
mkdir -p %{buildroot}%{_bindir}
ln -s %{_bindir}/consolehelper %{buildroot}%{_bindir}/gedit-root

%clean
rm -rf %{buildroot}

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
%{_sysconfdir}/pam.d/%{name}


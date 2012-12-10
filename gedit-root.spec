Name:		gedit-root
Summary:	Lets you launch gedit as root from the menu
Version:	1.0
Release:	%mkrel 7
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

%if %mdkversion < 200900
%post
%{update_desktop_database}
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%endif

%files
%defattr(-, root, root)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_sysconfdir}/security/console.apps/%{name}
%{_sysconfdir}/pam.d/%{name}



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-7mdv2011.0
+ Revision: 618446
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0-6mdv2010.0
+ Revision: 429189
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0-5mdv2009.0
+ Revision: 245876
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0-3mdv2008.1
+ Revision: 140735
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 12 2007 Adam Williamson <awilliamson@mandriva.org> 1.0-3mdv2008.0
+ Revision: 84756
- add /etc/pam.d file (#30957)
- remove X-Mandriva category from .desktop file
- spec clean

* Fri Apr 27 2007 Adam Williamson <awilliamson@mandriva.org> 1.0-2mdv2008.0
+ Revision: 18465
- Import gedit-root


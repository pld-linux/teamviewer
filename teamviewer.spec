# TODO
# - use system wine (bundles unmodified wine 1.1.41)
Summary:	TeamViewer Remote Control Application
Name:		teamviewer
Version:	7.0.9350
Release:	0.2
License:	Proprietary; includes substantial Free Software components, notably the Wine Project.
Group:		Applications/Networking
URL:		http://www.teamviewer.com/
Source0:	http://www.teamviewer.com/download/teamviewer_linux.tar.gz#/%{name}-%{version}.tgz
# NoSource0-md5:	8dc67cd8184b520e2e1b28d2afaa95bf
NoSource:	0
Source1:	%{name}.sh
Source2:	%{name}.desktop
Source3:	%{name}.png
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_libdir}/%{name}

# generate no Provides from private modules
%define		_noautoprovfiles	%{_libdir}/%{name}/.wine

# objects already stripped
%define		no_install_post_strip	1
%define		_enable_debug_packages	0

%description
TeamViewer is a remote control application free for private use. To
buy a license for commercial use, visit the webpage.

%prep
%setup -q -n %{name}7
install -p %{SOURCE1} teamviewer

#ver=$(strings ".wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer.exe" | grep %{version})
#test "$ver" = "%{version}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_bindir},%{_desktopdir},%{_pixmapsdir}}
cp -a .wine $RPM_BUILD_ROOT%{_appdir}
install -p teamviewer $RPM_BUILD_ROOT%{_appdir}/teamviewer
ln -s %{_appdir}/teamviewer $RPM_BUILD_ROOT%{_bindir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc license_foss.txt
%doc %lang(de) *_DE.txt
%doc %lang(en) *_EN.txt
%attr(755,root,root) %{_bindir}/teamviewer
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%dir %{_appdir}
%attr(755,root,root) %{_appdir}/teamviewer

# XXX: you need to chown wine dir for wine to work
%dir %{_appdir}/.wine

%dir %{_appdir}/.wine/drive_c
%dir %{_appdir}/.wine/drive_c/Program?Files
%dir %{_appdir}/.wine/drive_c/Program?Files/TeamViewer
%dir %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7
%doc %lang(en) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/License.txt
%doc %lang(de) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/Lizenz.txt
%attr(755,root,root) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer.exe
%attr(755,root,root) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Desktop.exe
%{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_StaticRes.dll
%attr(755,root,root) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/tvwine.dll.so
%lang(bg) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_bg.dll
%lang(cs) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_cs.dll
%lang(da) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_da.dll
%lang(de) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_de.dll
%lang(en) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_en.dll
%lang(es) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_es.dll
%lang(fi) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_fi.dll
%lang(fr) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_fr.dll
%lang(hr) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_hr.dll
%lang(hu) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_hu.dll
%lang(id) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_id.dll
%lang(it) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_it.dll
%lang(lt) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_lt.dll
%lang(nl) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_nl.dll
%lang(no) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_no.dll
%lang(pl) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_pl.dll
%lang(pt) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_pt.dll
%lang(ro) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_ro.dll
%lang(ru) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_ru.dll
%lang(sk) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_sk.dll
%lang(sr) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_sr.dll
%lang(sv) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_sv.dll
%lang(tr) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_tr.dll
%lang(uk) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version7/TeamViewer_Resource_uk.dll

# XXX: temp & ugly, until system wine works
%{_appdir}/.wine/share

# force +x bits
%defattr(755,root,root,755)
%{_appdir}/.wine/bin
%{_appdir}/.wine/lib

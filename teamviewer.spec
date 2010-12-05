# TODO
# - use system wine (bundles unmodified wine 1.1.41)
%define		buildid	9224
%define		rel		0.2
Summary:	TeamViewer Remote Control Application
Name:		teamviewer
Version:	6.0
Release:	%{buildid}.%{rel}
License:	Proprietary; includes substantial Free Software components, notably the Wine Project.
Group:		Applications/Networking
URL:		http://www.teamviewer.com/
Source0:	http://www.teamviewer.com/download/%{name}_linux.tar.gz
# NoSource0-md5:	9d139992beb7d72badbbb1759f81e734
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
%setup -q -n %{name}6
install -p %{SOURCE1} teamviewer.sh

ver=$(strings ".wine/drive_c/Program Files/TeamViewer/Version6/TeamViewer.exe" | grep %{version}.%{buildid})
test "$ver" = "%{version}.%{buildid}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_bindir},%{_desktopdir},%{_pixmapsdir}}
cp -a .wine $RPM_BUILD_ROOT%{_appdir}
install -p teamviewer $RPM_BUILD_ROOT%{_appdir}/teamviewer
ln -s %{_appdir}/teamviewer $RPM_BUILD_ROOT%{_bindir}
cp -a %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
cp -a %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

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
# XXX: temp & ugly, until system wine works
%defattr(755,root,root,755)
# XXX: you need to chown wine dir for wine to work
%dir %{_appdir}/.wine
%{_appdir}/.wine/*.reg
%{_appdir}/.wine/*.ppd
%{_appdir}/.wine/bin
%{_appdir}/.wine/dosdevices
%{_appdir}/.wine/lib
%{_appdir}/.wine/share
%dir %{_appdir}/.wine/drive_c
%{_appdir}/.wine/drive_c/windows
%dir %{_appdir}/.wine/drive_c/Program?Files
%dir %{_appdir}/.wine/drive_c/Program?Files/TeamViewer
%dir %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version6
%attr(755,root,root) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version6/TeamViewer.exe
%attr(755,root,root) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version6/tvwine.dll.so
%lang(ar) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version6/TeamViewer_Resource_ar.dll
%lang(cs) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version6/TeamViewer_Resource_cs.dll
%lang(da) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version6/TeamViewer_Resource_da.dll
%lang(de) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version6/TeamViewer_Resource_de.dll
%lang(en) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version6/TeamViewer_Resource_en.dll
%lang(es) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version6/TeamViewer_Resource_es.dll
%lang(fi) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version6/TeamViewer_Resource_fi.dll
%lang(fr) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version6/TeamViewer_Resource_fr.dll
%lang(it) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version6/TeamViewer_Resource_it.dll
%lang(ja) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version6/TeamViewer_Resource_ja.dll
%lang(ko) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version6/TeamViewer_Resource_ko.dll
%lang(nl) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version6/TeamViewer_Resource_nl.dll
%lang(no) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version6/TeamViewer_Resource_no.dll
%lang(pl) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version6/TeamViewer_Resource_pl.dll
%lang(pt) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version6/TeamViewer_Resource_pt.dll
%lang(ru) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version6/TeamViewer_Resource_ru.dll
%lang(sv) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version6/TeamViewer_Resource_sv.dll
%lang(tr) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version6/TeamViewer_Resource_tr.dll
%lang(zh) %{_appdir}/.wine/drive_c/Program?Files/TeamViewer/Version6/TeamViewer_Resource_zh.dll

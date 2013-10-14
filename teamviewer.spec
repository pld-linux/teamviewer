# TODO
# - use system wine (bundles unmodified wine 1.1.41)
%define		mver	8
Summary:	TeamViewer Remote Control Application
Name:		teamviewer
Version:	%{mver}.0.20931
Release:	0.3
License:	Proprietary; includes substantial Free Software components, notably the Wine Project.
Group:		Applications/Networking
Source0:	http://download.teamviewer.com/download/teamviewer_linux.tar.gz/%{name}-%{version}.tgz
# NoSource0-md5:	0b06c2ba7575c132eb2c6a6a4a41466b
NoSource:	0
URL:		http://www.teamviewer.com/
Source1:	%{name}.sh
Source2:	%{name}.desktop
BuildRequires: sed >= 4.0
Source3:	%{name}.png
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_libdir}/%{name}
%define		_winedir	%{_appdir}/wine

# generate no Provides from private modules
%define		_noautoprovfiles	%{_winedir}

# objects already stripped
%define		no_install_post_strip	1
%define		_enable_debug_packages	0

%description
TeamViewer is a remote control application free for private use. To
buy a license for commercial use, visit the webpage.

%prep
%setup -q -n %{name}%{mver}
install -p %{SOURCE1} %{name}.sh

ver=$(awk -F'"' '/^TV_VERSION/ {print $2}' tv_bin/script/tvw_config)
test "$ver" = "%{version}"

# simplify %doc
mv doc/* .

# move, to simplify install
mv tv_bin/wine .
mv wine/drive_c/TeamViewer .
mv tv_bin/desktop/* .

# want xdg user dirs
sed -i -e 's,TV_PKGTYPE="TAR",TV_PKGTYPE="RPM",' tv_bin/script/tvw_config

# wine docs
install -d wine-doc
mv wine/{AUTHORS,COPYING.LIB,LICENSE,README,VERSION} wine-doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_bindir},%{_desktopdir},%{_pixmapsdir}}
cp -a tv_bin/{TeamViewer*,teamviewerd,script} $RPM_BUILD_ROOT%{_appdir}
cp -a TeamViewer/* $RPM_BUILD_ROOT%{_appdir}
cp -a wine $RPM_BUILD_ROOT%{_appdir}
ln -s %{_appdir} $RPM_BUILD_ROOT%{_winedir}/drive_c/TeamViewer

cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
cp -p teamviewer.png $RPM_BUILD_ROOT%{_pixmapsdir}

%if 0
install -p %{name}.sh $RPM_BUILD_ROOT%{_appdir}/%{name}
ln -s %{_appdir}/%{name} $RPM_BUILD_ROOT%{_bindir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc license_foss.txt
%doc %lang(de) *_DE.txt Lizenz.txt
%doc %lang(en) *_EN.txt License.txt
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%if 0
%attr(755,root,root) %{_bindir}/teamviewer
%endif

%dir %{_appdir}
%doc %lang(en) %{_appdir}/License.txt
%doc %lang(de) %{_appdir}/Lizenz.txt
%attr(755,root,root) %{_appdir}/teamviewerd
%attr(755,root,root) %{_appdir}/TeamViewer.exe
%attr(755,root,root) %{_appdir}/TeamViewer
%attr(755,root,root) %{_appdir}/TeamViewer_Desktop
%attr(755,root,root) %{_appdir}/TeamViewer_Desktop.exe
%{_appdir}/TeamViewer_StaticRes.dll
%attr(755,root,root) %{_appdir}/tvwine.dll.so
%{_appdir}/TeamViewer_Resource_en.dll
%lang(bg) %{_appdir}/TeamViewer_Resource_bg.dll
%lang(cs) %{_appdir}/TeamViewer_Resource_cs.dll
%lang(da) %{_appdir}/TeamViewer_Resource_da.dll
%lang(de) %{_appdir}/TeamViewer_Resource_de.dll
%lang(es) %{_appdir}/TeamViewer_Resource_es.dll
%lang(fi) %{_appdir}/TeamViewer_Resource_fi.dll
%lang(fr) %{_appdir}/TeamViewer_Resource_fr.dll
%lang(hr) %{_appdir}/TeamViewer_Resource_hr.dll
%lang(hu) %{_appdir}/TeamViewer_Resource_hu.dll
%lang(id) %{_appdir}/TeamViewer_Resource_id.dll
%lang(it) %{_appdir}/TeamViewer_Resource_it.dll
%lang(lt) %{_appdir}/TeamViewer_Resource_lt.dll
%lang(nl) %{_appdir}/TeamViewer_Resource_nl.dll
%lang(no) %{_appdir}/TeamViewer_Resource_no.dll
%lang(pl) %{_appdir}/TeamViewer_Resource_pl.dll
%lang(pt) %{_appdir}/TeamViewer_Resource_pt.dll
%lang(ro) %{_appdir}/TeamViewer_Resource_ro.dll
%lang(ru) %{_appdir}/TeamViewer_Resource_ru.dll
%lang(sk) %{_appdir}/TeamViewer_Resource_sk.dll
%lang(sr) %{_appdir}/TeamViewer_Resource_sr.dll
%lang(sv) %{_appdir}/TeamViewer_Resource_sv.dll
%lang(tr) %{_appdir}/TeamViewer_Resource_tr.dll
%lang(uk) %{_appdir}/TeamViewer_Resource_uk.dll

%{_appdir}/script

# XXX: you need to chown wine dir for wine to work
%dir %{_winedir}

%dir %{_winedir}/drive_c
%dir %{_winedir}/drive_c/TeamViewer

%dir %{_winedir}/drive_c/windows
%dir %{_winedir}/drive_c/windows/system32
%{_winedir}/drive_c/windows/system32/winemenubuilder.exe

# XXX: temp & ugly, until system wine works
%{_winedir}/share

# force +x bits
%defattr(755,root,root,755)
%{_winedir}/bin
%{_winedir}/lib

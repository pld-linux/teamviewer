# TODO
# - use system wine (bundles unmodified wine 1.1.41)
%define		buildid	8888
%define		rel		0.1
Summary:	TeamViewer Remote Control Application
Name:		teamviewer
Version:	5.0
Release:	%{buildid}.%{rel}
License:	Proprietary; includes substantial Free Software components, notably the Wine Project.
Group:		Applications/Networking
Source0:	http://www.teamviewer.com/download/%{name}_linux.tar.gz
# NoSource0-md5:	10ba96fd81ac520f66c0f52cf70836a0
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
%setup -q -n %{name}5
install -p %{SOURCE1} teamviewer

ver=$(strings ".wine/drive_c/Program Files/TeamViewer/Version5/TeamViewer.exe" | grep %{version}.%{buildid})
if [ -z "$ver" ]; then
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_bindir},%{_desktopdir},%{_pixmapsdir}}
cp -a .wine teamviewer $RPM_BUILD_ROOT%{_appdir}
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
%{_appdir}/.wine

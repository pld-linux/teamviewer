# TODO
# - use system wine
# - desktop file
Summary:	TeamViewer Remote Control Application
Name:		teamviewer
Version:	5.0
Release:	0.3
License:	Proprietary; includes substantial Free Software components, notably the Wine Project.
Group:		Applications/Networking
Source0:	http://www.teamviewer.com/download/%{name}_linux.tar.gz
# NoSource0-md5:	2ff6ec6410f61b8f5d96d2057d00f886
NoSource:	0
Source1:	%{name}.sh
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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_bindir}}
cp -a .wine teamviewer $RPM_BUILD_ROOT%{_appdir}
ln -s %{_appdir}/teamviewer $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc license_teamviewer_en.txt copyrights_en.txt license_foss.txt
%doc %lang(de) copyrights_de.txt linux_faq_de.txt
%attr(755,root,root) %{_bindir}/teamviewer
%dir %{_appdir}
%attr(755,root,root) %{_appdir}/teamviewer
# XXX: temp & ugly, until system wine works
%defattr(755,root,root,755)
# XXX: you need to chown wine dir for wine to work
%{_appdir}/.wine

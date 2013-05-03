#
# TODO : clean up and move some to sitesctiptdir and fill more desc
Summary:	sK1 - illustration program
Summary(pl.UTF-8):	sK1 - program do ilustracji
Name:		sk1
Version:	0.9.1
Release:	0.2
License:	GPL v2
Group:		Applications/Communications
Source0:	https://sk1.googlecode.com/files/%{name}-0.9.1pre2_rev1383.tar.gz
# Source0-md5:	ce8a98e99e133b215b7ed67d6b0e0113
URL:		http://www.sk1project.org/
BuildRequires:	cairo-devel
BuildRequires:	lcms-devel
BuildRequires:	pkgconfig >= 1:0.21-2
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-devel >= 1:%py_ver
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	tk-devel
BuildRequires:	xorg-lib-libXext-devel
%pyrequires_eq	python = %py_ver
Requires:	python-PIL
Requires:	python-lcms
Requires:	python-sk1libs >= 0.9.1
Requires:	python-sk1sdk >= 0.9.1
Requires:	python-tkinter
#Suggests:	bluez-gnome
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sK1 illustration program

* cdr support (Corel 7 - X3)

%description -l pl.UTF-8
sK1 to program do ilustracji

* wsparcie dla plikow cdr (Corel 7 - X3)

%prep
%setup -q -n sk1-%{version}pre2

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

#% find_lang % {name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
#-f %{name}.lang
%defattr(644,root,root,755)
#%doc AUTHORS FAQ README
%attr(755,root,root) %{_bindir}/*
%dir %py_sitedir/sk1
%{py_sitedir}/sk1/*
%{py_sitedir}/*.egg-info

%{_pixmapsdir}/%{name}.png
%{_pixmapsdir}/%{name}.xpm
%{_desktopdir}/%{name}.desktop

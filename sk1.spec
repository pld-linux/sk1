#
# TODO : clean up and move some to sitesctiptdir and fill more desc
Summary:	sK1 - illustration program
Summary(pl.UTF-8):	sK1 - program do ilustracji
Name:		sk1
Version:	0.9.1
Release:	0.1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://www.sk1project.org/downloads/sk1/0.9.1pre_rev730/%{name}-%{version}pre_rev730.tar.gz
# Source0-md5:	723dbc0ef9b5426a8e9d4b132421c838
URL:		http://www.sk1project.org/
BuildRequires:	pkgconfig >= 1:0.21-2
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-devel >= 1:%py_ver
BuildRequires:	cairo-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	tk-devel
%pyrequires_eq	python = %py_ver
Requires:	python-PIL
Requires:	python-lcms
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
%setup -q -n sK1-%{version}pre

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
#%{_pixmapsdir}/%{name}.*
%dir %py_sitedir/sk1
%{py_sitedir}/sk1/*
%{py_sitedir}/*.egg-info
#%{_desktopdir}/%{name}.desktop

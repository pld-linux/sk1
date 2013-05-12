# TODO: move resources to /usr/share?
Summary:	sK1 - illustration program
Summary(pl.UTF-8):	sK1 - program do ilustracji
Name:		sk1
Version:	0.9.1
%define	subver	pre2
Release:	0.%{subver}.2
License:	GPL v2
Group:		Applications/Communications
Source0:	https://sk1.googlecode.com/files/%{name}-%{version}%{subver}_rev1383.tar.gz
# Source0-md5:	ce8a98e99e133b215b7ed67d6b0e0113
URL:		http://www.sk1project.org/
BuildRequires:	cairo-devel
BuildRequires:	lcms-devel
BuildRequires:	pkgconfig >= 1:0.21-2
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	tk-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
%pyrequires_eq	python
Requires:	python-PIL
Requires:	python-lcms
Requires:	python-sk1libs >= 0.9.1
Requires:	python-sk1sdk >= 0.9.1
Requires:	python-tkinter
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sK1 is an open source vector graphics editor similar to CorelDRAW(TM),
Adobe(R) Illustrator(TM), or Adobe(R) Freehand(TM). First of all sK1
is oriented for prepress industry.

It features CDR support (Corel 7 - X3).

%description -l pl.UTF-8
sK1 to mający otwarte źródła program do grafiki wektorowej, podobny do
programów CorelDRAW(TM), Adobe(R) Illustrator(TM), Adobe(R)
Freehand(TM). sK1 jest zorientowany przede wszystkim dla etapu
studyjnego (prepress).

Możliwości programu obejmują obsługę plików CDR (Corel 7 - X3).

%prep
%setup -q -n sk1-%{version}%{subver}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

# COPYRIGHTS packages as %doc, the rest in common-licenses
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/sk1/{COPYRIGHTS,GNU_GPL_v2,GNU_LGPL_v2}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README src/COPYRIGHTS
%attr(755,root,root) %{_bindir}/sk1
%dir %{py_sitedir}/sk1
%{py_sitedir}/sk1/__init__.py[co]
%dir %{py_sitedir}/sk1/app
%{py_sitedir}/sk1/app/Graphics
%{py_sitedir}/sk1/app/Lib
%{py_sitedir}/sk1/app/Scripting
%{py_sitedir}/sk1/app/UI
%{py_sitedir}/sk1/app/X11
%{py_sitedir}/sk1/app/conf
%{py_sitedir}/sk1/app/events
%{py_sitedir}/sk1/app/io
%{py_sitedir}/sk1/app/managers
%dir %{py_sitedir}/sk1/app/modules
%attr(755,root,root) %{py_sitedir}/sk1/app/modules/*.so
%{py_sitedir}/sk1/app/modules/descr.txt
%{py_sitedir}/sk1/app/scripts
%{py_sitedir}/sk1/app/tcl
%{py_sitedir}/sk1/app/utils
%{py_sitedir}/sk1/app/VERSION
%{py_sitedir}/sk1/app/__init__.py[co]
%{py_sitedir}/sk1/app/main.py[co]
%{py_sitedir}/sk1/app/skapp.py[co]
%dir %{py_sitedir}/sk1/share
%{py_sitedir}/sk1/share/cursors
%dir %{py_sitedir}/sk1/share/locales
%lang(da) %{py_sitedir}/sk1/share/locales/da
%lang(de) %{py_sitedir}/sk1/share/locales/de
%lang(es) %{py_sitedir}/sk1/share/locales/es
%lang(fr) %{py_sitedir}/sk1/share/locales/fr
%lang(it) %{py_sitedir}/sk1/share/locales/it
%lang(pt) %{py_sitedir}/sk1/share/locales/pt
%lang(pt_BR) %{py_sitedir}/sk1/share/locales/pt_BR
%lang(ru) %{py_sitedir}/sk1/share/locales/ru
%lang(rw) %{py_sitedir}/sk1/share/locales/rw
%lang(sv) %{py_sitedir}/sk1/share/locales/sv
%lang(uk) %{py_sitedir}/sk1/share/locales/uk
%lang(zh_TW) %{py_sitedir}/sk1/share/locales/zh_TW
%{py_sitedir}/sk1/share/palettes
%{py_sitedir}/sk1/share/ps_templates
%{py_sitedir}/sk1/share/resources
%{py_sitedir}/sk1-%{version}%{subver}-py*.egg-info
%{_pixmapsdir}/%{name}.png
%{_pixmapsdir}/%{name}.xpm
%{_desktopdir}/%{name}.desktop

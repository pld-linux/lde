Name:		lde
Version:	2.5.1
Release:	1
Summary:	Linux Disk Editor
Summary(pl):	Edytor systemów plików
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
License:	GPL
URL:		http://www.datafoundation.org/lde/
Source0:	http://www.datafoundation.org/lde/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	ncurses-devel
BuildRequires:	gpm-devel

%description
This package allows you to view some Linux fs's (a la Norton disk
edit), hex block and inode editing are now supported and you can use
it to dump and erased file to another partition. Supports ext2, minix,
xiafs, and generic binary editor mode.

%description -l pl
Pakiet pozwala na ogl±danie niektórych linuksowych systemów plików (w
sposób podobny do programu Norton diskedit). Mo¿e byæ u¿yty do
odzyskania skasowanych plików. Obs³uguje ext2, minix, xiafs oraz
zwyk³y tryb binarny.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

%{__make} install \
	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf README* TODO WARNING doc/UNERASE src/ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%doc *.gz doc/*.gz doc/*.tex src/*.gz

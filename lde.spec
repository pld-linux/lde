Summary:	Linux Disk Editor
Summary(pl):	Edytor system�w plik�w
Name:		lde
Version:	2.6.0
Release:	3
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/lde/%{name}-%{version}CVS.tar.gz
# Source0-md5:	ba554c2b1365f52f6ace6490a98afc7b
URL:		http://sourceforge.net/projects/lde/
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows you to view some Linux fs's (a la Norton disk
edit), hex block and inode editing are now supported and you can use
it to dump and erased file to another partition. Supports ext2, minix,
xiafs, and generic binary editor mode.

%description -l pl
Pakiet pozwala na ogl�danie niekt�rych linuksowych system�w plik�w (w
spos�b podobny do programu Norton diskedit). Mo�e by� u�yty do
odzyskania skasowanych plik�w. Obs�uguje ext2, minix, xiafs oraz
zwyk�y tryb binarny.

%prep
%setup -q -n %{name}

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

%{__make} install \
	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.tex README* TODO WARNING doc/UNERASE src/ChangeLog
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*

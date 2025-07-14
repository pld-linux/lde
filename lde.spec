Summary:	Linux Disk Editor
Summary(pl.UTF-8):	Edytor systemów plików
Name:		lde
Version:	2.6.1
Release:	5
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/lde/%{name}-%{version}.tar.gz
# Source0-md5:	7cd3a798cafc07d084db240fd1d1c830
Patch0:		%{name}-fix.patch
URL:		http://lde.sourceforge.net/
BuildRequires:	bison
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows you to view some Linux fs's (a la Norton disk
edit), hex block and inode editing are now supported and you can use
it to dump and erased file to another partition. Supports ext2, minix,
xiafs, and generic binary editor mode.

%description -l pl.UTF-8
Pakiet pozwala na oglądanie niektórych linuksowych systemów plików (w
sposób podobny do programu Norton diskedit). Może być użyty do
odzyskania skasowanych plików. Obsługuje ext2, minix, xiafs oraz
zwykły tryb binarny.

%prep
%setup -q -n %{name}
%patch -P0 -p1

%build
%configure \
	LIBS="-ltinfo"
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

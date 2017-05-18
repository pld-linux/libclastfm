#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	Unofficial C-API for the Last.fm web service
Summary(pl.UTF-8):	Nieoficjalne API C usługi WWW Last.fm
Name:		libclastfm
Version:	0.5
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/liblastfm/%{name}-%{version}.tar.gz
# Source0-md5:	0a71c485726a7e8970b970f520508a9b
URL:		http://liblastfm.sourceforge.net/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libclastfm is an unofficial C-API for the Last.fm web service written
with libcurl. It was written because the official CBS Interactive
Last.fm library requires Qt, which is usually not desired when using
GTK+ based distros.

This library supports much more than basic scrobble submission. You
can send shouts, fetch Album covers and much more.

Due to the naming conflict with the official last.fm library, this
library will install as "libclastfm".

%description -l pl.UTF-8
libclastfm to nieoficjalne API języka C do usługi WWW Last.fm,
napisane z użyciem biblioteki libcurl. Powstało, ponieważ oficjalna
biblioteka CBS Interactive Last.fm wymaga biblioteki Qt, która jest
zwykle niepożądana w przypadku korzystania z dystrybucji opartych na
GTK+.

Biblioteka ta obsługuje dużo więcej, niż proste wysyłanie swoich
preferencji (scrobble); można wysyłać okrzyki, pobierać okładki
albumów itp.

Ze względu na konflikt nazw z oficjalną biblioteką last.fm, ta jest
instalowana pod nazwą "libclastfm".

%package devel
Summary:	Development files for libclastfm
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libcflastfm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel

%description devel
This package contains files for developing applications that use
libclastfm.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki do tworzenia aplikacji wykorzystujących
bibliotekę libclastfm.

%package static
Summary:	Static libclastfm library
Summary(pl.UTF-8):	Statyczna biblioteka libclastfm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libclastfm library.

%description static -l pl.UTF-8
Statyczna biblioteka libclastfm.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libclastfm.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libclastfm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclastfm.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclastfm.so
%{_includedir}/clastfm.h
%{_pkgconfigdir}/libclastfm.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libclastfm.a
%endif


%define	git_snapshot 1

%if 0%{?git_snapshot}
%define	git_rev 968af0ab84e6f8b7658371c778fc8ad2714db68e
%define	git_date 20120314
%define	git_short %(echo %{git_rev} | cut -c-8)
%define	git_version %{git_date}git%{git_short}
%endif

# Source0 was generated as follows:
# git clone git://liblastfm.git.sourceforge.net/gitroot/liblastfm/liblastfm
# cd %{name}
# git archive --format=tar --prefix=%{name}/ %{git_short} | bzip2 > %{name}-%{?git_version}.tar.bz2

Summary:	Unofficial C-API for the Last.fm web service
Name:		libclastfm
Version:	0.5
Release:	0.1%{?git_version:.%{?git_version}}
License:	GPL v3+
Group:		Libraries
URL:		http://liblastfm.sourceforge.net/
Source0:	%{name}-%{git_version}.tar.bz2
# Source0-md5:	2e17a7981e2f16b9533994e543ed318a
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libclastfm is an unofficial C-API for the Last.fm web service written
with libcurl. It was written because the official CBS Interactive
Last.fm library requires Nokia QT, which is usually not desired when
using GTK+ based distros.

This library supports much more than basic scrobble submission. You
can send shouts, fetch Album covers and much more.

Due to the naming conflict with the official last.fm library, this
library will install as "libclastfm".

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains libraries and header files for developing
applications that use %{name}.

%prep
%setup -qn %{name}

%build
%{__aclocal}
%{__libtoolize}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name '*.la' | xargs rm -v

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README
%attr(755,root,root) %{_libdir}/libclastfm.so.*.*.*
%ghost %{_libdir}/libclastfm.so.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/clastfm.h
%{_libdir}/%{name}.so
%{_pkgconfigdir}/%{name}.pc

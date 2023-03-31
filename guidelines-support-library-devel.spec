# Typically referred to as GSL -- but that acronym is already
# taken by the much older GNU Scientific Library
Name:		guidelines-support-library-devel
Summary:	Guidelines Support Library
Version:	4.0.0
Release:	2
Group:		Development/C
License:	MIT
Url:		https://github.com/microsoft/GSL
Source0:	https://github.com/microsoft/GSL/archive/v%{version}/GSL-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja
BuildArch:	noarch

%description
The Guidelines Support Library (GSL) contains functions and types that are
suggested for use by the C++ Core Guidelines maintained by the Standard
C++ Foundation. This repo contains Microsoft's implementation of GSL.

The library includes types like span<T>, string_span, owner<> and others.

The entire implementation is provided inline in the headers under the gsl
directory. The implementation generally assumes a platform that implements
C++14 support.

While some types have been broken out into their own headers
(e.g. gsl/span), it is simplest to just include gsl/gsl and gain access
to the entire library.

%prep
%autosetup -p1 -n GSL-%{version}
# GSL_TEST is disabled because it pulls in a download of googletest
%cmake -G Ninja \
	-DBUILD_GMOCK:BOOL=OFF \
	-DGSL_TEST:BOOL=OFF \
	-DINSTALL_GTEST:BOOL=OFF

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_includedir}/gsl
%{_datadir}/cmake/Microsoft.GSL

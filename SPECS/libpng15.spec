Summary: Old version of libpng, needed to run old binaries
Name: libpng15
Version: 1.5.30
Release: 7%{?dist}
License: zlib
URL: http://www.libpng.org/pub/png/

# Note: non-current tarballs get moved to the history/ subdirectory,
# so look there if you fail to retrieve the version you want
Source0: https://ftp-osl.osuosl.org/pub/libpng/src/libpng15/libpng-%{version}.tar.xz

Source1: pngusr.dfa

Patch0: libpng15-CVE-2013-6954.patch
Patch1: libpng15-CVE-2018-13785.patch

BuildRequires: gcc
BuildRequires: zlib-devel

%description
The libpng15 package provides libpng 1.5, an older version of the libpng.
library for manipulating PNG (Portable Network Graphics) image format files.
This version should be used only if you are unable to use the current
version of libpng.

%prep
%setup -q -n libpng-%{version}

%patch0 -p1
%patch1 -p1

# Provide pngusr.dfa for build.
cp -p %{SOURCE1} .

%build
%configure --disable-static
make %{?_smp_mflags} DFA_XTRA=pngusr.dfa

%install
make DESTDIR=$RPM_BUILD_ROOT install

# We don't ship .la files.
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_libdir}/libpng*.so
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libpng.pc
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libpng15.pc
rm -rf $RPM_BUILD_ROOT%{_mandir}/*
rm -rf $RPM_BUILD_ROOT%{_includedir}/*
rm -rf $RPM_BUILD_ROOT%{_bindir}/*

%files
%doc LICENSE
%{_libdir}/libpng15.so.*

%changelog
* Thu Jun 06 2019 Nikola Forró <nforro@redhat.com> - 1.5.30-7
- New package for RHEL 8.1.0
  resolves: #1687581

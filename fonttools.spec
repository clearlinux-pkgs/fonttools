#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v21
# autospec commit: f35655a
#
Name     : fonttools
Version  : 4.55.0
Release  : 148
URL      : https://github.com/fonttools/fonttools/archive/4.55.0/fonttools-4.55.0.tar.gz
Source0  : https://github.com/fonttools/fonttools/archive/4.55.0/fonttools-4.55.0.tar.gz
Summary  : Tools to manipulate font files
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT OFL-1.1
Requires: fonttools-bin = %{version}-%{release}
Requires: fonttools-license = %{version}-%{release}
Requires: fonttools-man = %{version}-%{release}
Requires: fonttools-python = %{version}-%{release}
Requires: fonttools-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(brotli)
BuildRequires : pypi(brotlicffi)
BuildRequires : pypi(fs)
BuildRequires : pypi(glyphslib)
BuildRequires : pypi(lxml)
BuildRequires : pypi(munkres)
BuildRequires : pypi(py)
BuildRequires : pypi(scipy)
BuildRequires : pypi(sympy)
BuildRequires : pypi(ufolib2)
BuildRequires : pypi(uharfbuzz)
BuildRequires : pypi(zopfli)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Remove-ufo2ft-not-required-for-tests.patch

%description
The *.txt data in this directory was imported from:
https://github.com/Monotype/OpenType_Table_Source/tree/gh-pages/downloads

%package bin
Summary: bin components for the fonttools package.
Group: Binaries
Requires: fonttools-license = %{version}-%{release}

%description bin
bin components for the fonttools package.


%package license
Summary: license components for the fonttools package.
Group: Default

%description license
license components for the fonttools package.


%package man
Summary: man components for the fonttools package.
Group: Default

%description man
man components for the fonttools package.


%package python
Summary: python components for the fonttools package.
Group: Default
Requires: fonttools-python3 = %{version}-%{release}

%description python
python components for the fonttools package.


%package python3
Summary: python3 components for the fonttools package.
Group: Default
Requires: python3-core
Provides: pypi(fonttools)
Requires: pypi(brotli)
Requires: pypi(brotlicffi)
Requires: pypi(fs)
Requires: pypi(glyphslib)
Requires: pypi(lxml)
Requires: pypi(munkres)
Requires: pypi(scipy)
Requires: pypi(sympy)
Requires: pypi(ufolib2)
Requires: pypi(uharfbuzz)
Requires: pypi(zopfli)

%description python3
python3 components for the fonttools package.


%prep
%setup -q -n fonttools-4.55.0
cd %{_builddir}/fonttools-4.55.0
%patch -P 1 -p1
pushd ..
cp -a fonttools-4.55.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1731624082
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fonttools
cp %{_builddir}/fonttools-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/fonttools/3b4f969a237019242665f7adacc882c35a82c145 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fonttools
/usr/bin/pyftmerge
/usr/bin/pyftsubset
/usr/bin/ttx

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fonttools/3b4f969a237019242665f7adacc882c35a82c145

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ttx.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

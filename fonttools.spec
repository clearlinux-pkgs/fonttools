#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fonttools
Version  : 4.4.1
Release  : 42
URL      : https://github.com/fonttools/fonttools/archive/4.4.1/fonttools-4.4.1.tar.gz
Source0  : https://github.com/fonttools/fonttools/archive/4.4.1/fonttools-4.4.1.tar.gz
Summary  : Tools to manipulate font files
Group    : Development/Tools
License  : MIT OFL-1.1
Requires: fonttools-bin = %{version}-%{release}
Requires: fonttools-license = %{version}-%{release}
Requires: fonttools-man = %{version}-%{release}
Requires: fonttools-python = %{version}-%{release}
Requires: fonttools-python3 = %{version}-%{release}
Requires: brotli
Requires: brotlipy
Requires: fs
Requires: lxml
Requires: munkres
Requires: scipy
Requires: unicodedata2
Requires: zopfli
BuildRequires : brotli
BuildRequires : brotlipy
BuildRequires : buildreq-distutils3
BuildRequires : fs
BuildRequires : lxml
BuildRequires : munkres
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : scipy
BuildRequires : tox
BuildRequires : unicodedata2
BuildRequires : virtualenv
BuildRequires : zopfli

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

%description python3
python3 components for the fonttools package.


%prep
%setup -q -n fonttools-4.4.1
cd %{_builddir}/fonttools-4.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582924839
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fonttools
cp %{_builddir}/fonttools-4.4.1/LICENSE %{buildroot}/usr/share/package-licenses/fonttools/3b4f969a237019242665f7adacc882c35a82c145
cp %{_builddir}/fonttools-4.4.1/LICENSE.external %{buildroot}/usr/share/package-licenses/fonttools/9e8dedfa954e04fa103507441dcd4010c90ddedd
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

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
/usr/share/package-licenses/fonttools/9e8dedfa954e04fa103507441dcd4010c90ddedd

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ttx.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

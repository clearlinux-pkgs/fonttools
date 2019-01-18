#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fonttools
Version  : 3.36.0
Release  : 10
URL      : https://github.com/fonttools/fonttools/archive/3.36.0.tar.gz
Source0  : https://github.com/fonttools/fonttools/archive/3.36.0.tar.gz
Summary  : No detailed summary available
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
Requires: scipy
Requires: zopfli
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
The *.txt data in this directory was imported from:
https://github.com/Monotype/OpenType_Table_Source/tree/gh-pages/downloads

%package bin
Summary: bin components for the fonttools package.
Group: Binaries
Requires: fonttools-license = %{version}-%{release}
Requires: fonttools-man = %{version}-%{release}

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

%description python3
python3 components for the fonttools package.


%prep
%setup -q -n fonttools-3.36.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547823844
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fonttools
cp LICENSE %{buildroot}/usr/share/package-licenses/fonttools/LICENSE
cp LICENSE.external %{buildroot}/usr/share/package-licenses/fonttools/LICENSE.external
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fonttools
/usr/bin/pyftinspect
/usr/bin/pyftmerge
/usr/bin/pyftsubset
/usr/bin/ttx

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fonttools/LICENSE
/usr/share/package-licenses/fonttools/LICENSE.external

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ttx.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cereal
Version  : 1.3.1
Release  : 6
URL      : https://github.com/USCiLab/cereal/archive/refs/tags/v1.3.1.tar.gz
Source0  : https://github.com/USCiLab/cereal/archive/refs/tags/v1.3.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause BSL-1.0
Requires: cereal-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : llvm

%description
cereal - A C++11 header only library for serialization
======================================================
cereal takes arbitrary data types and reversibly turns them into different representations,
such as compact binary encodings, XML, or JSON. cereal was designed to be fast, light-weight,
and easy to extend - it has no external dependencies and can be easily bundled with other code
or used standalone.

%package dev
Summary: dev components for the cereal package.
Group: Development
Provides: cereal-devel = %{version}-%{release}
Requires: cereal = %{version}-%{release}

%description dev
dev components for the cereal package.


%package license
Summary: license components for the cereal package.
Group: Default

%description license
license components for the cereal package.


%prep
%setup -q -n cereal-1.3.1
cd %{_builddir}/cereal-1.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1643909233
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CC=clang
export CXX=clang++
export LD=ld.gold
CFLAGS=${CFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
CXXFLAGS=${CXXFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
unset LDFLAGS
export AR=llvm-ar
export RANLIB=llvm-ranlib
export NM=llvm-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto "
%cmake .. -DSKIP_PORTABILITY_TEST=ON -DWITH_WERROR=OFF
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1643909233
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cereal
cp %{_builddir}/cereal-1.3.1/LICENSE %{buildroot}/usr/share/package-licenses/cereal/6d638dc6b507800038c3148dc3dcef0b6a638890
cp %{_builddir}/cereal-1.3.1/include/cereal/external/rapidjson/msinttypes/LICENSE %{buildroot}/usr/share/package-licenses/cereal/4be0fd49db3887f68fd61b5a8239205d8ce75deb
cp %{_builddir}/cereal-1.3.1/include/cereal/external/rapidxml/license.txt %{buildroot}/usr/share/package-licenses/cereal/0173e4174701724de9b9a5b258d59066215a9ff3
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/cereal/access.hpp
/usr/include/cereal/archives/adapters.hpp
/usr/include/cereal/archives/binary.hpp
/usr/include/cereal/archives/json.hpp
/usr/include/cereal/archives/portable_binary.hpp
/usr/include/cereal/archives/xml.hpp
/usr/include/cereal/cereal.hpp
/usr/include/cereal/details/helpers.hpp
/usr/include/cereal/details/polymorphic_impl.hpp
/usr/include/cereal/details/polymorphic_impl_fwd.hpp
/usr/include/cereal/details/static_object.hpp
/usr/include/cereal/details/traits.hpp
/usr/include/cereal/details/util.hpp
/usr/include/cereal/external/LICENSE
/usr/include/cereal/external/base64.hpp
/usr/include/cereal/external/rapidjson/LICENSE
/usr/include/cereal/external/rapidjson/allocators.h
/usr/include/cereal/external/rapidjson/cursorstreamwrapper.h
/usr/include/cereal/external/rapidjson/document.h
/usr/include/cereal/external/rapidjson/encodedstream.h
/usr/include/cereal/external/rapidjson/encodings.h
/usr/include/cereal/external/rapidjson/error/en.h
/usr/include/cereal/external/rapidjson/error/error.h
/usr/include/cereal/external/rapidjson/filereadstream.h
/usr/include/cereal/external/rapidjson/filewritestream.h
/usr/include/cereal/external/rapidjson/fwd.h
/usr/include/cereal/external/rapidjson/internal/biginteger.h
/usr/include/cereal/external/rapidjson/internal/diyfp.h
/usr/include/cereal/external/rapidjson/internal/dtoa.h
/usr/include/cereal/external/rapidjson/internal/ieee754.h
/usr/include/cereal/external/rapidjson/internal/itoa.h
/usr/include/cereal/external/rapidjson/internal/meta.h
/usr/include/cereal/external/rapidjson/internal/pow10.h
/usr/include/cereal/external/rapidjson/internal/regex.h
/usr/include/cereal/external/rapidjson/internal/stack.h
/usr/include/cereal/external/rapidjson/internal/strfunc.h
/usr/include/cereal/external/rapidjson/internal/strtod.h
/usr/include/cereal/external/rapidjson/internal/swap.h
/usr/include/cereal/external/rapidjson/istreamwrapper.h
/usr/include/cereal/external/rapidjson/memorybuffer.h
/usr/include/cereal/external/rapidjson/memorystream.h
/usr/include/cereal/external/rapidjson/msinttypes/LICENSE
/usr/include/cereal/external/rapidjson/msinttypes/inttypes.h
/usr/include/cereal/external/rapidjson/msinttypes/stdint.h
/usr/include/cereal/external/rapidjson/ostreamwrapper.h
/usr/include/cereal/external/rapidjson/pointer.h
/usr/include/cereal/external/rapidjson/prettywriter.h
/usr/include/cereal/external/rapidjson/rapidjson.h
/usr/include/cereal/external/rapidjson/reader.h
/usr/include/cereal/external/rapidjson/schema.h
/usr/include/cereal/external/rapidjson/stream.h
/usr/include/cereal/external/rapidjson/stringbuffer.h
/usr/include/cereal/external/rapidjson/writer.h
/usr/include/cereal/external/rapidxml/license.txt
/usr/include/cereal/external/rapidxml/manual.html
/usr/include/cereal/external/rapidxml/rapidxml.hpp
/usr/include/cereal/external/rapidxml/rapidxml_iterators.hpp
/usr/include/cereal/external/rapidxml/rapidxml_print.hpp
/usr/include/cereal/external/rapidxml/rapidxml_utils.hpp
/usr/include/cereal/macros.hpp
/usr/include/cereal/specialize.hpp
/usr/include/cereal/types/array.hpp
/usr/include/cereal/types/atomic.hpp
/usr/include/cereal/types/base_class.hpp
/usr/include/cereal/types/bitset.hpp
/usr/include/cereal/types/boost_variant.hpp
/usr/include/cereal/types/chrono.hpp
/usr/include/cereal/types/common.hpp
/usr/include/cereal/types/complex.hpp
/usr/include/cereal/types/concepts/pair_associative_container.hpp
/usr/include/cereal/types/deque.hpp
/usr/include/cereal/types/forward_list.hpp
/usr/include/cereal/types/functional.hpp
/usr/include/cereal/types/list.hpp
/usr/include/cereal/types/map.hpp
/usr/include/cereal/types/memory.hpp
/usr/include/cereal/types/optional.hpp
/usr/include/cereal/types/polymorphic.hpp
/usr/include/cereal/types/queue.hpp
/usr/include/cereal/types/set.hpp
/usr/include/cereal/types/stack.hpp
/usr/include/cereal/types/string.hpp
/usr/include/cereal/types/tuple.hpp
/usr/include/cereal/types/unordered_map.hpp
/usr/include/cereal/types/unordered_set.hpp
/usr/include/cereal/types/utility.hpp
/usr/include/cereal/types/valarray.hpp
/usr/include/cereal/types/variant.hpp
/usr/include/cereal/types/vector.hpp
/usr/include/cereal/version.hpp
/usr/lib64/cmake/cereal/cerealConfig.cmake
/usr/lib64/cmake/cereal/cerealConfigVersion.cmake
/usr/lib64/cmake/cereal/cerealTargets.cmake

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cereal/0173e4174701724de9b9a5b258d59066215a9ff3
/usr/share/package-licenses/cereal/4be0fd49db3887f68fd61b5a8239205d8ce75deb
/usr/share/package-licenses/cereal/6d638dc6b507800038c3148dc3dcef0b6a638890

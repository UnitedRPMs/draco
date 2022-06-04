%global debug_package %{nil}
%global  _hardened_build     1
#define _legacy_common_support 1
%global _disable_ld_no_undefined %nil
%undefine __cmake_in_source_build


# draco git
%global commit0 4cba1acdd718b700bb33945c0258283689d4eac7
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver git%{shortcommit0}



Name: draco
Version: 1.5.2
Release: 1%{?dist}

License: ASL 2.0
URL: https://github.com/google/draco
Summary: A library for compressing and decompressing 3D geometric meshes and point clouds 
Source0: https://github.com/google/draco/archive/refs/tags/%{version}.tar.gz

ExclusiveArch: x86_64

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ninja-build


%description
A library for compressing and decompressing 3D geometric meshes and point clouds

%package devel
Summary: Development files for draco
Requires: draco >= %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{version} 


%build
  mkdir -p build
    cmake -B build -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INTERPROCEDURAL_OPTIMIZATION=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=ON 
    


  %ninja_build -C build -j2

%install
   
  %ninja_install -C build  -j2

  rm -f %{buildroot}/%{_libdir}/libdraco.a

%files

%{_bindir}/draco_decoder
%{_bindir}/draco_decoder-1.5.2
%{_bindir}/draco_encoder
%{_bindir}/draco_encoder-1.5.2
%{_libdir}/libdraco.so.4
%{_libdir}/libdraco.so.4.0.0


%files devel
%{_includedir}/draco/
%{_datadir}/cmake/
%{_libdir}/libdraco.so
%{_libdir}/pkgconfig/draco.pc

%changelog

* Wed Jun 01 2022 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.5.2-1
- Inital build

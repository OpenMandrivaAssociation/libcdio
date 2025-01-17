%define build_vcd 0
%{?_with_vcd: %{expand: %%global build_vcd 1}}
%{?_without_vcd: %{expand: %%global build_vcd 0}}

%define major 19
%define libname %mklibname cdio %{major}

%define isomajor 11
%define libiso %mklibname iso9660_ %{isomajor}

%define ppmajor 1
%define libnamepp %mklibname cdio++ %{ppmajor}

%define isoppmajor 0
%define libisopp %mklibname iso++ %{isoppmajor}

%define udfmajor 0
%define libudf %mklibname udf %{udfmajor}

%define devname %mklibname -d cdio

Summary:	CD-ROM reading library
Name:		libcdio
Version:	2.1.0
Release:	2
License:	GPLv3+
Group:		System/Libraries
Url:		https://www.gnu.org/software/libcdio/
Source0:	ftp://ftp.gnu.org/pub/gnu/libcdio/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.gnu.org/pub/gnu/libcdio/%{name}-%{version}.tar.bz2.sig

BuildRequires:	pkgconfig(libcddb)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(popt)
#gw only if we change the man pages
#BuildRequires: help2man
%if %build_vcd
BuildRequires:	pkgconfig(libvcdinfo)
%endif

%description 
This library is to encapsulate CD-ROM reading and
control. Applications wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

Some support for disk image types like BIN/CUE and NRG is available,
so applications that use this library also have the ability to read
disc images as though they were CD's.

%package apps
Summary:	Example tool from %{name}
Group:		Sound
Provides:	libcdio0-apps

%description apps
This library is to encapsulate CD-ROM reading and
control. Applications wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

Some support for disk image types like BIN/CUE and NRG is available,
so applications that use this library also have the ability to read
disc images as though they were CD's.

This contains the program cd-info as an example application of %{name}.

%package -n %{libname}
Summary:	Library from %{name}
Group:		System/Libraries
Provides:	libcdio = %{version}-%{release}
Obsoletes:	%{mklibname cdio 13} <= 0.83

%description -n %{libname}
This package contains the library for libcdio.

%package -n %{libiso}
Summary:	Library from %{name}
Group:		System/Libraries

%description -n %{libiso}
This package contains the library for libiso.

%package -n %{libnamepp}
Summary:	C++ library from %{name}
Group:		System/Libraries

%description -n %{libnamepp}
This package contains the C++ library for libcdio++.

%package -n %{libisopp}
Summary:	C++ library from %{name}
Group:		System/Libraries
Conflicts:	%{_lib}cdiopp0 < 0.90-1

%description -n %{libisopp}
This package contains the C++ library for libiso++.

%package -n %{libudf}
Summary:	Libraries from %{name}
Group:		System/Libraries

%description -n %{libudf}
This package contains the library for libudf.

%package -n %{devname}
Summary:	Devel files from %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libiso} = %{version}-%{release}
Requires:	%{libnamepp} = %{version}-%{release}
Requires:	%{libisopp} = %{version}-%{release}
Requires:	%{libudf} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}cdio-static-devel

%description -n %{devname}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	--disable-rpath \
	--without-versioned-libs \
%if ! %build_vcd
	--disable-vcd-info
%endif

%make_build

%install
%make_install

%files apps
%doc README AUTHORS
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libcdio.so.%{major}*

%files -n %{libiso}
%{_libdir}/libiso9660.so.%{isomajor}*

%files -n %{libudf}
%{_libdir}/libudf.so.%{udfmajor}*

%files -n %{libnamepp}
%{_libdir}/libcdio++.so.%{ppmajor}*

%files -n %{libisopp}
%{_libdir}/libiso9660++.so.%{isoppmajor}*

%files -n %{devname}
%doc ChangeLog README AUTHORS INSTALL TODO
%{_includedir}/cdio
%{_includedir}/cdio++/
%{_infodir}/libcdio.info*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libcdio.pc
%{_libdir}/pkgconfig/libcdio++.pc
%{_libdir}/pkgconfig/libiso9660.pc
%{_libdir}/pkgconfig/libiso9660++.pc
%{_libdir}/pkgconfig/libudf.pc

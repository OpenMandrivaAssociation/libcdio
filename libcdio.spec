%define build_vcd 1
%{?_with_vcd: %{expand: %%global build_vcd 1}}
%{?_without_vcd: %{expand: %%global build_vcd 0}}

%define major	13
%define libname %mklibname cdio %{major}
%define devname %mklibname -d cdio
%define statname %mklibname -d -s cdio

%define isomajor 8
%define isolibname %mklibname iso9660_ %{isomajor}
%define cddamajor 1
%define cddalibname %mklibname cdio_cdda %{cddamajor}
%define cdioppmajor 0
%define cdiopplibname %mklibname cdio++ %{cdioppmajor}
%define udfmajor 0
%define udflibname %mklibname udf %{udfmajor}

Summary:	CD-ROM reading library
Name:		libcdio
Version:	0.90
Release:	1
License:	GPLv3+
Group:		System/Libraries
URL:		http://www.gnu.org/software/libcdio/
Source0:	ftp://ftp.gnu.org/pub/gnu/libcdio/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.gnu.org/pub/gnu/libcdio/%{name}-%{version}.tar.gz.sig

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
Summary:	Libraries from %{name}
Group:		System/Libraries
Provides:	libcdio = %{version}-%{release}

%description -n %{libname}
This library is to encapsulate CD-ROM reading and
control. Applications wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

Some support for disk image types like BIN/CUE and NRG is available,
so applications that use this library also have the ability to read
disc images as though they were CD's.

%package -n %{isolibname}
Summary:	Libraries from %{name}
Group:		System/Libraries

%description -n %{isolibname}
This library is to encapsulate CD-ROM reading and
control. Applications wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

Some support for disk image types like BIN/CUE and NRG is available,
so applications that use this library also have the ability to read
disc images as though they were CD's.

%package -n %{cddalibname}
Summary:	Libraries from %{name}
Group:		System/Libraries

%description -n %{cddalibname}
This library is to encapsulate CD-ROM reading and
control. Applications wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

Some support for disk image types like BIN/CUE and NRG is available,
so applications that use this library also have the ability to read
disc images as though they were CD's.

%package -n %{cdiopplibname}
Summary:	C++ library from %{name}
Group:		System/Libraries

%description -n %{cdiopplibname}
This library is to encapsulate CD-ROM reading and
control. Applications wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

Some support for disk image types like BIN/CUE and NRG is available,
so applications that use this library also have the ability to read
disc images as though they were CD's.

%package -n %{udflibname}
Summary:	Libraries from %{name}
Group:		System/Libraries
Conflicts:	%{mklibname cdio_cdda 0}

%description -n %{udflibname}
This library is to encapsulate CD-ROM reading and
control. Applications wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

Some support for disk image types like BIN/CUE and NRG is available,
so applications that use this library also have the ability to read
disc images as though they were CD's.

%package -n %{devname}
Summary:	Devel files from %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{isolibname} = %{version}-%{release}
Requires:	%{cddalibname} = %{version}-%{release}
Requires:	%{cdiopplibname} = %{version}-%{release}
Requires:	%{udflibname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}cdio-static-devel

%description -n %{devname}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--without-versioned-libs \
%if ! %build_vcd
	--disable-vcd-info
%endif

%make

%install
%makeinstall_std
#gw was not installed:
cp libcdio_cdda.pc libcdio_paranoia.pc %{buildroot}%{_libdir}/pkgconfig
cd %{buildroot}%{_mandir}
mv jp ja

%files apps
%doc README AUTHORS NEWS INSTALL TODO
%{_bindir}/*
%{_mandir}/man1/*
%lang(ja) %{_mandir}/ja/man1/*

%files -n %{libname}
%_libdir/libcdio.so.%{major}*

%files -n %{isolibname}
%{_libdir}/libiso9660.so.%{isomajor}*

%files -n %{cddalibname}
%{_libdir}/libcdio_cdda.so.%{cddamajor}*
%{_libdir}/libcdio_paranoia.so.%{cddamajor}*

%files -n %{udflibname}
%{_libdir}/libudf.so.%{udfmajor}*

%files -n %{cdiopplibname}
%{_libdir}/libcdio++.so.%{cdioppmajor}*
%{_libdir}/libiso9660++.so.%{cdioppmajor}*

%files -n %{devname}
%doc ChangeLog README AUTHORS NEWS INSTALL TODO
%{_includedir}/cdio
%{_includedir}/cdio++/
%{_infodir}/libcdio.info*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libcdio.pc
%{_libdir}/pkgconfig/libcdio++.pc
%{_libdir}/pkgconfig/libcdio_cdda.pc
%{_libdir}/pkgconfig/libcdio_paranoia.pc
%{_libdir}/pkgconfig/libiso9660.pc
%{_libdir}/pkgconfig/libiso9660++.pc
%{_libdir}/pkgconfig/libudf.pc


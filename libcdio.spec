%define name libcdio
%define version 0.81
%define release %mkrel 2

%define build_vcd 1
%{?_with_vcd: %{expand: %%global build_vcd 1}}
%{?_without_vcd: %{expand: %%global build_vcd 0}}

%define major 10
%define libname %mklibname cdio %{major}
%define libnamedev %mklibname -d cdio
%define libnamestaticdev %mklibname -d -s cdio
%define isomajor 7
%define isolibname %mklibname iso9660_ %isomajor
%define cddamajor 0
%define cddalibname %mklibname cdio_cdda %cddamajor
%define cdioppmajor 0
%define cdiopplibname %mklibname cdio++ %cdioppmajor

Name: %name
Version: %version
Release: %release
License: GPLv3+
Group: System/Libraries
URL: http://www.gnu.org/software/libcdio/
Source: ftp://ftp.gnu.org/pub/gnu/libcdio/%name-%version.tar.gz
Patch: libcdio-0.81-fix-linking.patch
BuildRoot: %_tmppath/%name-buildroot
Summary: CD-ROM reading library
BuildRequires: libcddb-devel
BuildRequires: popt-devel
BuildRequires: libncurses-devel
#gw only if we change the man pages
#BuildRequires: help2man
%if %build_vcd
BuildRequires: libvcd-devel > 0.7.19
%endif

%description 
This library is to encapsulate CD-ROM reading and
control. Applications wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

Some support for disk image types like BIN/CUE and NRG is available,
so applications that use this library also have the ability to read
disc images as though they were CD's.


%package apps
Summary: Example tool from %name
Group: Sound
Provides: libcdio0-apps
Obsoletes: libcdio0-apps
 
%description apps
This library is to encapsulate CD-ROM reading and
control. Applications wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

Some support for disk image types like BIN/CUE and NRG is available,
so applications that use this library also have the ability to read
disc images as though they were CD's.

This contains the program cd-info as an example application of %name.

%package -n %{libname}
Summary: Libraries from %name
Group: System/Libraries
Provides: libcdio = %version-%release

%description -n %{libname}
This library is to encapsulate CD-ROM reading and
control. Applications wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

Some support for disk image types like BIN/CUE and NRG is available,
so applications that use this library also have the ability to read
disc images as though they were CD's.


%package -n %{libnamedev}
Summary: Devel files from %name
Group: Development/C
Requires: %{libname} = %version
Requires: %{isolibname} = %version
Requires: %{cddalibname} = %version
Requires: %{cdiopplibname} = %version
Provides: %name-devel = %version-%release 
Obsoletes: %mklibname -d cdio 7

 
%description -n %{libnamedev}
This is the libraries, include files and other resources you can use
to incorporate %name into applications.

%package -n %libnamestaticdev
Summary: Static Library for developing applications with %name
Group: Development/C
Requires: %libnamedev = %version
Obsoletes: %mklibname -d -s cdio 7

%description -n %libnamestaticdev
This contains the static library of %name needed for building apps that
link statically to %name.

%package -n %{isolibname}
Summary: Libraries from %name
Group: System/Libraries
Conflicts: libcdio < 0.74-2mdk

%description -n %{isolibname}
This library is to encapsulate CD-ROM reading and
control. Applications wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

Some support for disk image types like BIN/CUE and NRG is available,
so applications that use this library also have the ability to read
disc images as though they were CD's.

%package -n %{cddalibname}
Summary: Libraries from %name
Group: System/Libraries
Conflicts: libcdio < 0.74-2mdk

%description -n %{cddalibname}
This library is to encapsulate CD-ROM reading and
control. Applications wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

Some support for disk image types like BIN/CUE and NRG is available,
so applications that use this library also have the ability to read
disc images as though they were CD's.

%package -n %cdiopplibname
Summary: C++ library from %name
Group: System/Libraries

%description -n %{cdiopplibname}
This library is to encapsulate CD-ROM reading and
control. Applications wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

Some support for disk image types like BIN/CUE and NRG is available,
so applications that use this library also have the ability to read
disc images as though they were CD's.


%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %name-%version
%patch -p1 -b .fix-linking
aclocal -I m4
autoconf
automake
libtoolize

%build
%configure2_5x \
--without-versioned-libs \
%if ! %build_vcd
--disable-vcd-info
%endif

make

%install
rm -rf %buildroot
%makeinstall_std
#gw was not installed:
cp libcdio_cdda.pc libcdio_paranoia.pc %buildroot%_libdir/pkgconfig
cd %buildroot%_mandir
mv jp ja


%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{isolibname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{isolibname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{cddalibname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{cddalibname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{cdiopplibname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{cdiopplibname} -p /sbin/ldconfig
%endif


%post -n %{libnamedev}
%_install_info libcdio.info

%preun -n %{libnamedev}
%_remove_install_info libcdio.info

%files apps
%defattr(-,root,root)
%doc ChangeLog COPYING README AUTHORS NEWS INSTALL TODO
%_bindir/*
%_mandir/man1/*
%lang(ja) %_mandir/ja/man1/*

%files -n %{libname}
%defattr (- ,root,root)
%_libdir/libcdio.so.%{major}*

%files -n %{isolibname}
%defattr (- ,root,root)
%_libdir/libiso9660.so.%{isomajor}*

%files -n %{cddalibname}
%defattr (- ,root,root)
%_libdir/libcdio_cdda.so.%{cddamajor}*
%_libdir/libcdio_paranoia.so.%{cddamajor}*
%_libdir/libudf.so.%{cddamajor}*

%files -n %{libnamedev}
%defattr(-, root, root)
%doc ChangeLog COPYING README AUTHORS NEWS INSTALL TODO
%_includedir/cdio
%_includedir/cdio++/
%_infodir/libcdio.info*
%_libdir/*.so
%attr(644,root,root) %_libdir/*.la
%_libdir/pkgconfig/libcdio.pc
%_libdir/pkgconfig/libcdio_cdda.pc
%_libdir/pkgconfig/libcdio_paranoia.pc
%_libdir/pkgconfig/libiso9660.pc
%_libdir/pkgconfig/libudf.pc

%files -n %libnamestaticdev
%defattr(-,root,root)
%{_libdir}/lib*.a

%files -n %{cdiopplibname}
%defattr (- ,root,root)
%_libdir/libcdio++.so.%{cdioppmajor}*
%_libdir/libiso9660++.so.%{cdioppmajor}*

%clean
rm -rf ${RPM_BUILD_ROOT}



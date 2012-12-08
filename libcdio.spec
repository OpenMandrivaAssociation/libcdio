%define build_vcd 1
%{?_with_vcd: %{expand: %%global build_vcd 1}}
%{?_without_vcd: %{expand: %%global build_vcd 0}}

%define major 13
%define libname %mklibname cdio %{major}
%define libnamedev %mklibname -d cdio
%define libnamestaticdev %mklibname -d -s cdio
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
Version:	0.83
Release:	3
License:	GPLv3+
Group:		System/Libraries
URL:		http://www.gnu.org/software/libcdio/
Source:		ftp://ftp.gnu.org/pub/gnu/libcdio/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	popt-devel
BuildRequires:	pkgconfig(ncurses)
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

%package -n %{libnamedev}
Summary:	Devel files from %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{isolibname} = %{version}-%{release}
Requires:	%{cddalibname} = %{version}-%{release}
Requires:	%{cdiopplibname} = %{version}-%{release}
Requires:	%{udflibname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{libnamedev}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%package -n %{libnamestaticdev}
Summary:	Static Library for developing applications with %{name}
Group:		Development/C
Requires:	%{libnamedev} = %{version}

%description -n %{libnamestaticdev}
This contains the static library of %{name} needed for building apps that
link statically to %{name}.

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

%prep
%setup -q

%build
%configure2_5x \
--without-versioned-libs \
%if ! %build_vcd
--disable-vcd-info
%endif

make

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

%files -n %{libnamedev}
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

%files -n %{libnamestaticdev}
%{_libdir}/lib*.a

%files -n %{cdiopplibname}
%{_libdir}/libcdio++.so.%{cdioppmajor}*
%{_libdir}/libiso9660++.so.%{cdioppmajor}*

%changelog
* Wed May 02 2012 GÃ¶tz Waschk <waschk@mandriva.org> 0.83-2mdv2012.0
+ Revision: 794954
- remove libtool archives
- update build dep for ncurses
- yearly rebuild

* Thu Oct 27 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.83-1
+ Revision: 707530
- new version
- new major
- split out libudf
- spec cleanup

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 0.82-2
+ Revision: 660228
- mass rebuild

* Sat Nov 07 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.82-1mdv2011.0
+ Revision: 462458
- new version
- drop patches
- new major
- update file list

* Sun Oct 04 2009 Funda Wang <fwang@mandriva.org> 0.81-5mdv2010.0
+ Revision: 453447
- rebuild

  + Christophe Fergeau <cfergeau@mandriva.com>
    - rebuild

* Sat Apr 11 2009 Michael Scherer <misc@mandriva.org> 0.81-3mdv2009.1
+ Revision: 366171
- patch to fix endless loop when there is no cdrom, blocking xmms2
  among other, as reported on 49636
- add patch to clear format string error
- add missing libtoolize call

* Wed Oct 29 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.81-2mdv2009.1
+ Revision: 298224
- fix linking

* Mon Oct 27 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.81-1mdv2009.1
+ Revision: 297772
- fix build deps
- update file list
- new version
- new major
- update license
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Apr 15 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.80-2mdv2009.0
+ Revision: 193696
- add missing pkgconfig files

* Tue Apr 08 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.80-1mdv2009.0
+ Revision: 192411
- new version
- drop patch

* Fri Feb 08 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.79-3mdv2008.1
+ Revision: 163991
- replace Fedora patch by better Mandriva version

* Thu Jan 17 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.79-2mdv2008.1
+ Revision: 154097
- fix buffer overflow

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Oct 27 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.79-1mdv2008.1
+ Revision: 102571
- new version

* Thu Aug 30 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.78.2-1mdv2008.0
+ Revision: 75363
- new devel name


* Wed Nov 01 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.78.2-1mdv2007.0
+ Revision: 74975
- new version

* Sun Oct 29 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.78.1-1mdv2007.1
+ Revision: 73597
- new version
- new major
- Import libcdio

* Sat Oct 28 2006 Götz Waschk <waschk@mandriva.org> 0.78-1mdv2007.1
- new major
- New version 0.78

* Tue Sep 19 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 0.77-3mdv2007.0
- Rebuild

* Tue Mar 28 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.77-2mdk
- rebuild to fix apps package

* Sat Mar 18 2006 Götz Waschk <waschk@mandriva.org> 0.77-1mdk
- new majors
- add cdio++
- New release 0.77
- use mkrel

* Wed Oct 05 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.76-1mdk
- New release 0.76

* Fri Jul 22 2005 Götz Waschk <waschk@mandriva.org> 0.75-2mdk
- fix conflicts
- rebuild

* Tue Jul 12 2005 Götz Waschk <waschk@mandriva.org> 0.75-1mdk
- major 6
- reenable cddb

* Tue Jul 12 2005 Götz Waschk <waschk@mandriva.org> 0.74-2mdk
- disable cddb
- better split the package

* Sun May 15 2005 Götz Waschk <waschk@mandriva.org> 0.74-1mdk
- New release 0.74

* Tue Apr 19 2005 Götz Waschk <waschk@linux-mandrake.com> 0.73-2mdk
- rebuild for new libvcd

* Tue Apr 19 2005 Götz Waschk <waschk@linux-mandrake.com> 0.73-1mdk
- major 5
- New release 0.73

* Wed Feb 02 2005 Götz Waschk <waschk@linux-mandrake.com> 0.72-2mdk
- add conflict 
- reenable vcd

* Tue Feb 01 2005 Götz Waschk <waschk@linux-mandrake.com> 0.72-1mdk
- major 4
- update the file list
- disable vcdinfo
- drop the patch
- new version

* Thu Dec 30 2004 Angelo Naselli <anaselli@mandrake.org> 0.71-3mdk
- added patch needed to compile with c++
- added --without-versioned-libs to avoid problems linking 
  libcdio or libiso9660

* Mon Nov 22 2004 Götz Waschk <waschk@linux-mandrake.com> 0.71-2mdk
- rebuild

* Mon Nov 22 2004 Götz Waschk <waschk@linux-mandrake.com> 0.71-1mdk
- major 3
- disable parallel build
- New release 0.71

* Mon Nov 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.70-1mdk
- 0.70

* Sun Jun 27 2004 Götz Waschk <waschk@linux-mandrake.com> 0.69-1mdk
- fix source URL
- New release 0.69

* Sat Apr 03 2004 Götz Waschk <waschk@linux-mandrake.com> 0.68-2mdk
- new vcdimager

* Sat Apr 03 2004 Götz Waschk <waschk@linux-mandrake.com> 0.68-1mdk
- drop man pages
- new version

* Sat Jan 17 2004 Götz Waschk <waschk@linux-mandrake.com> 0.65-3mdk
- reenable vcd support

* Thu Jan 15 2004 Götz Waschk <waschk@linux-mandrake.com> 0.65-2mdk
- fix provides

* Thu Jan 15 2004 Götz Waschk <waschk@linux-mandrake.com> 0.65-1mdk
- use the mdkversion macro
- install man pages by hand
- disable vcdimager for now
- needs new vcdimager
- new version

* Thu Nov 20 2003 Götz Waschk <waschk@linux-mandrake.com> 0.64-3mdk
- update URL


%global date 20170905
%global _configure ../configure

Name:           npapi-vlc
Version:        2.2.7
Release:        0.1%{?date:snap%{date}}%{?dist}
Summary:        NPAPI plugin for libvlc

License:        LGPLv2+
URL:            https://code.videolan.org/videolan/npapi-vlc
#Source0:        http://download.videolan.org/videolan/vlc/%{version}/npapi-vlc-%{version}%{?githash}.tar.xz
Source0:        npapi-vlc-%{?date}.tar.xz

#Buildrequires:  libtool

BuildRequires:  gecko-devel
BuildRequires:  vlc-devel
Requires:       %{name}-filesystem = %{version}-%{release}

%description
NPAPI plugin for libvlc.

%package        filesystem
Summary:        NPAPI plugin for libvlc - filesystem
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description    filesystem
NPAPI plugin for libvlc - filesystem

%package        gtk
Summary:        NPAPI plugin for libvlc - gtk version
Requires:       %{name}-filesystem = %{version}-%{release}

%description    gtk
NPAPI plugin for libvlc - gtk version.


%prep
%setup -q -n npapi-vlc-%{?date}
autoreconf -sif


%build
mkdir -p generic gtk
pushd generic
%configure --disable-silent-rules --without-gtk

%make_build
popd

pushd gtk
%configure --disable-silent-rules

%make_build
popd

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/vlc/npapi
pushd generic
%make_install
mv $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins/libvlcplugin.so \
 $RPM_BUILD_ROOT%{_libdir}/vlc/npapi/libvlcplugin-generic.so
popd
pushd gtk
%make_install
mv $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins/libvlcplugin.so \
 $RPM_BUILD_ROOT%{_libdir}/vlc/npapi/libvlcplugin-gtk.so
popd
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

#Alternative support
touch $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins/libvlcplugin.so


%post
update-alternatives \
  --install \
    %{_libdir}/mozilla/plugins/libvlcplugin.so \
    libvlcplugin.so.%{_arch} \
    %{_libdir}/vlc/npapi/libvlcplugin-generic.so \
    200

%post gtk
update-alternatives \
  --install \
    %{_libdir}/mozilla/plugins/libvlcplugin.so \
    libvlcplugin.so.%{_arch} \
    %{_libdir}/vlc/npapi/libvlcplugin-gtk.so \
    100 \

%postun
alternatives --remove libvlcplugin.so.%{_arch} %{_libdir}/vlc/npapi/libvlcplugin-generic.so

%postun gtk
alternatives --remove libvlcplugin.so.%{_arch} %{_libdir}/vlc/npapi/libvlcplugin-gtk.so


%files filesystem
%doc AUTHORS ChangeLog COPYING NEWS
%dir %{_libdir}/vlc/npapi

%files
%ghost %{_libdir}/mozilla/plugins/libvlcplugin.so
%{_libdir}/vlc/npapi/libvlcplugin-generic.so

%files gtk
%ghost %{_libdir}/mozilla/plugins/libvlcplugin.so
%{_libdir}/vlc/npapi/libvlcplugin-gtk.so



%changelog
* Tue Sep 05 2017 Nicolas Chauvet <kwizart@gmail.com> - 2.2.7-0.1snap20170905
- Update snapshot
- Bump generic plugin over the gtk one

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.2.0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.2.0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 15 2014 Nicolas Chauvet <kwizart@gmail.com> - 2.2.0-0.1
- Update to 2.2.0

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jan 14 2014 Nicolas Chauvet <kwizart@gmail.com> - 2.0.6-2
- Drop gtk dependency from main

* Fri Apr 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.0.6-1
- Update to 2.0.6
- Add alternatives support for generic build
- Add mozilla-vlc to point to gtk sub-package

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.0.2-2
- Mass rebuilt for Fedora 19 Features

* Fri Mar  9 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Mon Jan 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-0.3gitf568362
- Restore Obsoletes mozilla-vlc

* Sun Jan 01 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-0.2gitf568362
- Update to today's snapshot

* Thu Dec 22 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-0.1git30357f8
- Initial package


#global githash f568362

Name:           npapi-vlc
Version:        2.0.2
Release:        2%{?githash:git%{githash}}%{?dist}
Summary:        NPAPI plugin for libvlc

Group:          Applications/Internet
License:        LGPLv2+
URL:            http://git.videolan.org/?p=npapi-vlc.git;a=summary
Source0:        http://download.videolan.org/videolan/vlc/%{version}/npapi-vlc-%{version}%{?githash}.tar.xz
Patch0:         npapi-vlc-master.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#Buildrequires:  libtool

BuildRequires:  gecko-devel
BuildRequires:  vlc-devel

Provides:       mozilla-vlc = %{version}-%{release}
Obsoletes:      mozilla-vlc < 1.2.0


%description
NPAPI plugin for libvlc.


%prep
%setup -q -n npapi-vlc-%{version}%{?githash}
%patch0 -p1


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS
%{_libdir}/mozilla/plugins/libvlcplugin.so



%changelog
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


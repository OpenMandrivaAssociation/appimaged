Name:           appimaged
Version:        10
Release:        1
URL:            https://www.appimage.org
Summary:        Daemon handles (un)registering AppImages with the system
License:        MIT
Group:          System/Daemons
Source0:        https://github.com/AppImageCommunity/appimaged/archive/refs/heads/appimaged-master.tar.gz
#Source1:        appimaged.service

BuildRequires:  cmake
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  inotify-tools-devel
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  libtool
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(liblzma)
Recommends:       zsync

%description
appimaged is a daemon that handles registering and unregistering AppImages
with the system (e.g., menu entries, icons, MIME types, binary delta updates,
and such).

The package comes also with appimage.validate CLI tool to verify signature
of AppImage files.

%prep
%setup -n appimaged-master


%build
%cmake

%make_build

%install
%make_install -C build 
#mkdir -p %{buildroot}%{_bindir}
#install -m 0755 appimaged appimage.validate %{buildroot}%{_bindir}

# install systemd per user service
#mkdir -p %{buildroot}%{_userunitdir}
#install -m 0644 %{SOURCE1} %{buildroot}%{_userunitdir}/appimaged.service

#%post
#%systemd_user_post appimaged.service

#%preun
#%systemd_user_preun appimaged.service

#%postun
#%systemd_user_postun appimaged.service

%files
%defattr(-,root,root)
%license LICENSE
%doc README.md
%{_bindir}/appimage.validate
%{_bindir}/appimaged
%{_userunitdir}/appimaged.service

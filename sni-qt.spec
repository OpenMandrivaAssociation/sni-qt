%define plugin %mklibname %{name}

Summary:	Qt4 plugin that turns QSystemTrayIcons into status notifiers (config)
Name:		sni-qt
Version:	0.2.6
Release:	2
License:	LGPLv3+
Group:		System/Libraries
Url:		https://launchpad.net/sni-qt
Source0:	https://launchpad.net/sni-qt/trunk/%{version}/+download/%{name}-%{version}.tar.bz2
# From Ubuntu packaging version 0.2.5-0ubuntu3
Source1:	sni-qt.conf
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(dbusmenu-qt)
Requires:	%{plugin}
# To support system tray for 32 bit applications in x86_64 system
%ifarch x86_64
Suggests:	sni-qt-32
%endif

%description
This package contains config for a Qt4 plugin which turns all QSystemTrayIcon
into StatusNotifierItems (appindicators).

%files
%doc COPYING NEWS README
%config %{_sysconfdir}/xdg/sni-qt.conf

#----------------------------------------------------------------------------

%package -n %{plugin}
Summary:	Qt4 plugin that turns QSystemTrayIcons into status notifiers (plugin)
Group:		System/Libraries
Requires:	%{name}
%ifarch x86_64
Provides:	sni-qt-64 = %{EVRD}
%else
Provides:	sni-qt-32 = %{EVRD}
%endif
Conflicts:	%{name} < 0.2.6-2

%description -n %{plugin}
This package contains a Qt4 plugin which turns all QSystemTrayIcon into
StatusNotifierItems (appindicators).

%files -n %{plugin}
%{_qt_plugindir}/systemtrayicon/

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build

install -m644 -D -p %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/sni-qt.conf


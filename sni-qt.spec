Summary:	Qt4 plugin that turns QSystemTrayIcons into status notifiers
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

%description
This package contains a Qt4 plugin which turns all QSystemTrayIcon into
StatusNotifierItems (appindicators).

%files
%doc COPYING NEWS README
%config %{_sysconfdir}/xdg/sni-qt.conf
%{_qt_plugindir}/systemtrayicon/

#------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build

install -m644 -D -p %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/sni-qt.conf


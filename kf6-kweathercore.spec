%define major 0
%define libname %mklibname KF6WeatherCore
%define devname %mklibname KF6WeatherCore -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kf6-kweathercore
Version:	0.8.0
Release:	2
#Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
#Source0:	https://invent.kde.org/libraries/kweathercore/-/archive/master/kweathercore-master.tar.bz2
Source0:	https://invent.kde.org/libraries/kweathercore/-/archive/v%{version}/kweathercore-v%{version}.tar.bz2
Summary: KDE library for handling weather data
URL: https://invent.kde.org/libraries/kweathercore
License: GPL
Group: System/Libraries
BuildRequires: appstream
BuildRequires: bison
BuildRequires: doxygen
BuildRequires: qt6-qttools
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Positioning)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Holidays)

%description
KDE library for handling weather data

%package -n %{libname}
Summary: KDE library for handling weather data
Group: System/Libraries

%description -n %{libname}
KDE library for handling weather data

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1 -n kweathercore-v%{version}
%cmake -G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kweathercore6

%files -n %{libname} 
%{_libdir}/*.so.%{major}*
%{_libdir}/*.so.6

%files -n %{devname} -f kweathercore6.lang
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_prefix}/mkspecs/modules/qt_KWeatherCore.pri


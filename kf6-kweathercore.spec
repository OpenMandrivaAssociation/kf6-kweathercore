%define major 0
%define libname %mklibname KF5WeatherCore
%define devname %mklibname KF5WeatherCore -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kweathercore
Version:	0.7
Release:	1
#Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
#Source0:	https://invent.kde.org/libraries/kweathercore/-/archive/master/kweathercore-master.tar.bz2
Source0:	https://invent.kde.org/libraries/kweathercore/-/archive/v%{version}/kweathercore-v%{version}.tar.bz2
Summary: KDE library for handling weather data
URL: https://invent.kde.org/libraries/kweathercore
License: GPL
Group: System/Libraries
BuildRequires: bison
BuildRequires: doxygen qt5-doc qt5-qttools qdoc5 qt5-assistant
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Positioning)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Holidays)

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
%autosetup -p1 -n %{name}-v%{version}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/*.so.5

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
%doc %{_docdir}/qt5/KF5KWeatherCore.qch
%doc %{_docdir}/qt5/KF5KWeatherCore.tags

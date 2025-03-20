#define date 20210206

Name: qt-heic-image-plugin
Version: 0.6.0
Release: %{?date:0.%{date}.}1
Source0: https://github.com/novomesk/qt-heic-image-plugin/archive/%{?date:master}%{!?date:v%{version}}/%{name}-%{version}.tar.gz
Summary: Qt plugin for working with HEIC image files
URL: https://github.com/novomesk/qt-heic-image-plugin
License: LGPLv3
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(libheif) >= 1.1
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: qt5-macros
BuildRequires: qmake5
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)

%description
Qt plugin for working with HEIC image files

%package qt5
Summary:	HEIC image file support for Qt 5.x
Group:		System/Libraries

%description qt5
HEIC image file support for Qt 5.x

%prep
%autosetup -p1 -n %{name}-%{?date:master}%{!?date:%{version}}
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

cd ..
export CMAKE_BUILD_DIR=build-qt5
%cmake \
	-DQT_MAJOR_VERSION=5 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build
%ninja_build -C build-qt5

%install
%ninja_install -C build-qt5
%ninja_install -C build

%files
%{_qtdir}/plugins/imageformats/kimg_heif6.so

%files qt5
%{_libdir}/qt5/plugins/imageformats/kimg_heif5.so
%{_datadir}/kservices5/qimageioplugins/heif.desktop

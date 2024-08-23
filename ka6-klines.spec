#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.08.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		klines
Summary:	klines
Name:		ka6-%{kaname}
Version:	24.08.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	36c95ceafb6669639d7b36afaa345d3a
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Qml-devel >= 5.11.1
BuildRequires:	Qt6Quick-devel >= 5.11.1
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	ka6-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KLines is a simple but highly addictive one player game. The player
has to move the colored balls around the game board, gathering them
into the lines of the same color by five. Once the line is complete it
is removed from the board, therefore freeing precious space.

%description -l pl.UTF-8
KLines jest prostą albo bardzo wciągającą grą dla jednej osoby. Gracz
ma przemieszczać kolorowe piłki po planszy, zbierając je po pięć w
linii jednego koloru. Kompletne linie są usuwane z planszy zwalniając
cenne miejsce.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klines
%{_desktopdir}/org.kde.klines.desktop
%{_datadir}/config.kcfg/klines.kcfg
%{_iconsdir}/hicolor/*x*/apps/klines.png
%{_datadir}/klines
%{_datadir}/metainfo/org.kde.klines.appdata.xml
%{_datadir}/qlogging-categories6/klines.categories
%{_datadir}/qlogging-categories6/klines.renamecategories

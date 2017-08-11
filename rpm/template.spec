Name:           ros-kinetic-catkin-pip
Version:        0.2.3
Release:        0%{?dist}
Summary:        ROS catkin_pip package

Group:          Development/Libraries
License:        BSD
URL:            http://github.com/asmodehn/catkin_pip
Source0:        %{name}-%{version}.tar.gz

Requires:       python-devel >= 2.7.5
Requires:       python-pip >= 1.5.4
BuildRequires:  git >= 1.9.1
BuildRequires:  python-devel >= 2.7.5
BuildRequires:  python-pip >= 1.5.4
BuildRequires:  ros-kinetic-catkin

%description
Catkin macros to allow using pure python packages in usual catkin workspaces
with normal python workflow.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Aug 11 2017 AlexV <asmodehn@gmail.com> - 0.2.3-0
- Autogenerated by Bloom

* Fri Aug 04 2017 AlexV <asmodehn@gmail.com> - 0.2.2-0
- Autogenerated by Bloom

* Tue May 16 2017 AlexV <asmodehn@gmail.com> - 0.2.1-0
- Autogenerated by Bloom

* Mon Mar 20 2017 AlexV <asmodehn@gmail.com> - 0.2.0-0
- Autogenerated by Bloom

* Fri Jan 13 2017 AlexV <asmodehn@gmail.com> - 0.1.17-0
- Autogenerated by Bloom

* Mon Sep 05 2016 AlexV <asmodehn@gmail.com> - 0.1.16-0
- Autogenerated by Bloom

* Fri Sep 02 2016 AlexV <asmodehn@gmail.com> - 0.1.15-0
- Autogenerated by Bloom

* Sat Aug 27 2016 AlexV <asmodehn@gmail.com> - 0.1.12-0
- Autogenerated by Bloom


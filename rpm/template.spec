Name:           ros-jade-ntpd-driver
Version:        1.1.1
Release:        0%{?dist}
Summary:        ROS ntpd_driver package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/ntpd_driver
Source0:        %{name}-%{version}.tar.gz

Requires:       poco-devel
Requires:       ros-jade-cmake-modules
Requires:       ros-jade-message-generation
Requires:       ros-jade-message-runtime
Requires:       ros-jade-roscpp
Requires:       ros-jade-sensor-msgs
BuildRequires:  poco-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cmake-modules
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-message-runtime
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-sensor-msgs

%description
ntpd_driver sends TimeReference message time to ntpd server

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sat Jul 18 2015 Vladimir Ermakov <vooon341@gmail.com> - 1.1.1-0
- Autogenerated by Bloom

* Fri Apr 17 2015 Vladimir Ermakov <vooon341@gmail.com> - 1.1.0-0
- Autogenerated by Bloom

* Wed Feb 25 2015 Vladimir Ermakov <vooon341@gmail.com> - 1.0.2-0
- Autogenerated by Bloom


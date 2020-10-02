#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : spdlog
Version  : 1.8.1
Release  : 3
URL      : https://github.com/gabime/spdlog/archive/v1.8.1/spdlog-1.8.1.tar.gz
Source0  : https://github.com/gabime/spdlog/archive/v1.8.1/spdlog-1.8.1.tar.gz
Summary  : Fast C++ logging library.
Group    : Development/Tools
License  : BSL-1.0 MIT
Requires: spdlog-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : fmt-dev
BuildRequires : glibc-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libsystemd)
BuildRequires : spdlog-dev

%description
# spdlog
Very fast, header-only/compiled, C++ logging library. [![Build Status](https://travis-ci.org/gabime/spdlog.svg?branch=v1.x)](https://travis-ci.org/gabime/spdlog)&nbsp; [![Build status](https://ci.appveyor.com/api/projects/status/d2jnxclg20vd0o50?svg=true)](https://ci.appveyor.com/project/gabime/spdlog) [![Release](https://img.shields.io/github/release/gabime/spdlog.svg)](https://github.com/gabime/spdlog/releases/latest)

%package dev
Summary: dev components for the spdlog package.
Group: Development
Provides: spdlog-devel = %{version}-%{release}
Requires: spdlog = %{version}-%{release}

%description dev
dev components for the spdlog package.


%package license
Summary: license components for the spdlog package.
Group: Default

%description license
license components for the spdlog package.


%prep
%setup -q -n spdlog-1.8.1
cd %{_builddir}/spdlog-1.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1601663986
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :

%install
export SOURCE_DATE_EPOCH=1601663986
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/spdlog
cp %{_builddir}/spdlog-1.8.1/LICENSE %{buildroot}/usr/share/package-licenses/spdlog/617ee17d495e6cb87f0d74cc2bddffaf5b827b1f
cp %{_builddir}/spdlog-1.8.1/include/spdlog/fmt/bundled/LICENSE.rst %{buildroot}/usr/share/package-licenses/spdlog/a6571b819c2fb290e2bb182e92a7a20d7d42318d
cp %{_builddir}/spdlog-1.8.1/tests/catch.license %{buildroot}/usr/share/package-licenses/spdlog/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/spdlog/async.h
/usr/include/spdlog/async_logger-inl.h
/usr/include/spdlog/async_logger.h
/usr/include/spdlog/cfg/argv.h
/usr/include/spdlog/cfg/env.h
/usr/include/spdlog/cfg/helpers-inl.h
/usr/include/spdlog/cfg/helpers.h
/usr/include/spdlog/common-inl.h
/usr/include/spdlog/common.h
/usr/include/spdlog/details/backtracer-inl.h
/usr/include/spdlog/details/backtracer.h
/usr/include/spdlog/details/circular_q.h
/usr/include/spdlog/details/console_globals.h
/usr/include/spdlog/details/file_helper-inl.h
/usr/include/spdlog/details/file_helper.h
/usr/include/spdlog/details/fmt_helper.h
/usr/include/spdlog/details/log_msg-inl.h
/usr/include/spdlog/details/log_msg.h
/usr/include/spdlog/details/log_msg_buffer-inl.h
/usr/include/spdlog/details/log_msg_buffer.h
/usr/include/spdlog/details/mpmc_blocking_q.h
/usr/include/spdlog/details/null_mutex.h
/usr/include/spdlog/details/os-inl.h
/usr/include/spdlog/details/os.h
/usr/include/spdlog/details/periodic_worker-inl.h
/usr/include/spdlog/details/periodic_worker.h
/usr/include/spdlog/details/registry-inl.h
/usr/include/spdlog/details/registry.h
/usr/include/spdlog/details/synchronous_factory.h
/usr/include/spdlog/details/tcp_client-windows.h
/usr/include/spdlog/details/tcp_client.h
/usr/include/spdlog/details/thread_pool-inl.h
/usr/include/spdlog/details/thread_pool.h
/usr/include/spdlog/details/windows_include.h
/usr/include/spdlog/fmt/bin_to_hex.h
/usr/include/spdlog/fmt/bundled/LICENSE.rst
/usr/include/spdlog/fmt/bundled/chrono.h
/usr/include/spdlog/fmt/bundled/color.h
/usr/include/spdlog/fmt/bundled/compile.h
/usr/include/spdlog/fmt/bundled/core.h
/usr/include/spdlog/fmt/bundled/format-inl.h
/usr/include/spdlog/fmt/bundled/format.h
/usr/include/spdlog/fmt/bundled/locale.h
/usr/include/spdlog/fmt/bundled/os.h
/usr/include/spdlog/fmt/bundled/ostream.h
/usr/include/spdlog/fmt/bundled/posix.h
/usr/include/spdlog/fmt/bundled/printf.h
/usr/include/spdlog/fmt/bundled/ranges.h
/usr/include/spdlog/fmt/chrono.h
/usr/include/spdlog/fmt/fmt.h
/usr/include/spdlog/fmt/ostr.h
/usr/include/spdlog/formatter.h
/usr/include/spdlog/fwd.h
/usr/include/spdlog/logger-inl.h
/usr/include/spdlog/logger.h
/usr/include/spdlog/pattern_formatter-inl.h
/usr/include/spdlog/pattern_formatter.h
/usr/include/spdlog/sinks/android_sink.h
/usr/include/spdlog/sinks/ansicolor_sink-inl.h
/usr/include/spdlog/sinks/ansicolor_sink.h
/usr/include/spdlog/sinks/base_sink-inl.h
/usr/include/spdlog/sinks/base_sink.h
/usr/include/spdlog/sinks/basic_file_sink-inl.h
/usr/include/spdlog/sinks/basic_file_sink.h
/usr/include/spdlog/sinks/daily_file_sink.h
/usr/include/spdlog/sinks/dist_sink.h
/usr/include/spdlog/sinks/dup_filter_sink.h
/usr/include/spdlog/sinks/msvc_sink.h
/usr/include/spdlog/sinks/null_sink.h
/usr/include/spdlog/sinks/ostream_sink.h
/usr/include/spdlog/sinks/ringbuffer_sink.h
/usr/include/spdlog/sinks/rotating_file_sink-inl.h
/usr/include/spdlog/sinks/rotating_file_sink.h
/usr/include/spdlog/sinks/sink-inl.h
/usr/include/spdlog/sinks/sink.h
/usr/include/spdlog/sinks/stdout_color_sinks-inl.h
/usr/include/spdlog/sinks/stdout_color_sinks.h
/usr/include/spdlog/sinks/stdout_sinks-inl.h
/usr/include/spdlog/sinks/stdout_sinks.h
/usr/include/spdlog/sinks/syslog_sink.h
/usr/include/spdlog/sinks/systemd_sink.h
/usr/include/spdlog/sinks/tcp_sink.h
/usr/include/spdlog/sinks/win_eventlog_sink.h
/usr/include/spdlog/sinks/wincolor_sink-inl.h
/usr/include/spdlog/sinks/wincolor_sink.h
/usr/include/spdlog/spdlog-inl.h
/usr/include/spdlog/spdlog.h
/usr/include/spdlog/stopwatch.h
/usr/include/spdlog/tweakme.h
/usr/include/spdlog/version.h
/usr/lib64/cmake/spdlog/spdlogConfig.cmake
/usr/lib64/cmake/spdlog/spdlogConfigTargets-relwithdebinfo.cmake
/usr/lib64/cmake/spdlog/spdlogConfigTargets.cmake
/usr/lib64/cmake/spdlog/spdlogConfigVersion.cmake
/usr/lib64/pkgconfig/spdlog.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/spdlog/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
/usr/share/package-licenses/spdlog/617ee17d495e6cb87f0d74cc2bddffaf5b827b1f
/usr/share/package-licenses/spdlog/a6571b819c2fb290e2bb182e92a7a20d7d42318d

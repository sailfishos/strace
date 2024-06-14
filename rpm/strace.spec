Name:       strace
Summary:    Tracks and displays system calls associated with a running process
Version:    6.9
Release:    1
License:    LGPLv2+
URL:        https://strace.io
Source0:    %{name}-%{version}.tar.xz

%description
The strace program intercepts and records the system calls called and
received by a running process.  Strace can print a record of each
system call, its arguments and its return value.  Strace is useful for
diagnosing problems and debugging, as well as for instructional
purposes.

Install strace if you need a tool to track the system calls made and
received by a process.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build

sh bootstrap
%reconfigure --enable-mpers=check
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
	install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} \
	        AUTHORS ChangeLog-CVS NEWS README

%files
%license COPYING
%{_bindir}/strace
%{_bindir}/strace-log-merge

%files doc
%{_mandir}/man*/*
%{_docdir}/%{name}-%{version}

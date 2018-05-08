Name:       strace
Summary:    Tracks and displays system calls associated with a running process
Version:    4.22
Release:    1
Group:      Development/Debuggers
License:    BSD
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

%package graph
Summary:   Create a graph from strace output
BuildArch: noarch
Requires:  strace = %{version}

%description graph
%{summary}.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build

sh bootstrap
%reconfigure --disable-static
make %{_smp_mflags}

%install
rm -rf %{buildroot}

%make_install

%files
%defattr(-,root,root,-)
%{_bindir}/strace
%{_bindir}/strace-log-merge
%{_mandir}/man1/*

%files graph
%defattr(-,root,root,-)
%{_bindir}/strace-graph

# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       mlspp

# >> macros
# << macros

Summary:    Template Project
Version:    0.1
Release:    0
Group:      Applications
License:    BSD-2-Clause
URL:        https://codeberg.org/nephros/template
Source0:    %{name}-%{version}.tar.gz
Source100:  mlspp.yaml
Source101:  mlspp-rpmlintrc
BuildRequires:  pkgconfig(openssl)
BuildRequires:  cmake
BuildRequires:  protobuf-lite-devel

%description


%if "%{?vendor}" == "chum"
Title: MLS++
DeveloperName: Cisco Systems
DeveloperLogin: cisco
PackagedBy: nephros
Categories:
 - Library
Custom:
  Repo: https://github.com/cisco/mlspp
Links:
  Homepage: %{url}
  Help: %{url}/discussions
  Bugtracker: %{url}/issues
%endif


%package client
Summary:    Development files for %{name}
Group:      Development
Requires:   %{name} = %{version}-%{release}

%description client
%{summary}.

%package devel
Summary:    Development files for %{name}
Group:      Development
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}.

%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre

%cmake . 
make %{?_smp_mflags}

# >> build post
make %{?_smp_mflags}
pushd cmd/interop
%cmake .
make %{?_smp_mflags}
popd
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
pushd cmd/interop
%make_install
make %{?_smp_mflags}
# << install post

%files
%defattr(-,root,root,-)
%license LICENSE
# >> files
# << files

%files client
%defattr(-,root,root,-)
%{_bindir}/%{name}_client
# >> files client
# << files client

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_includedir}/%{name}/*
%{_datadir}/%{name}
# >> files devel
# << files devel

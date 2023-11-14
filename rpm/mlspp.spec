# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       mlspp

# >> macros
# << macros

Summary:    Implementation of Messaging Layer Security
Version:    0.1
Release:    0
Group:      Development/Libraries
License:    BSD-2-Clause
URL:        https://github.com/cisco/mlspp
Source0:    %{name}-%{version}.tar.gz
Source100:  mlspp.yaml
Source101:  mlspp-rpmlintrc
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(openssl) >= 1.1.1
BuildRequires:  cmake
Provides:   cmake(%{name}-targets)
Provides:   cmake(%{name}-config)
Provides:   cmake(%{name}-config-version)

%description
%{summary}.

%if "%{?vendor}" == "chum"
Title: MLS++
DeveloperName: Cisco Systems
DeveloperLogin: cisco
PackagedBy: nephros
Categories:
 - Library
Custom:
  Repo: https://github.com/cisco/mlspp
  PackagingRepo: https://github.com/nephros/sailfish-mls
Links:
  Homepage: %{url}
  Help: %{url}/discussions
  Bugtracker: %{url}/issues
%endif


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# for SFOS 3.4, which has cmake 3.11.3.
# Then again, SFOS 3.4 does not have openssl 1.1 either so this is moot:
# sed -i 's/cmake_minimum_required(VERSION 3.12)/cmake_minimum_required(VERSION 3.11)/' CMakeLists.txt
# << build pre

%cmake . 
make %{?_smp_mflags}

# >> build post
# pushd cmd/interop
# %cmake .
# %make_build
# popd
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
#pushd cmd/interop
#%make_install
# popd
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license LICENSE
%{_libdir}/*.so
%{_includedir}/%{name}/*
%{_datadir}/%{name}
# >> files
# << files

# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       mls-client

# >> macros
# << macros

Summary:    Implementation of Messaging Layer Security
Version:    0.1
Release:    0
Group:      Development/Libraries
License:    BSD-2-Clause
URL:        https://github.com/cisco/mlspp
Source0:    mlspp-%{version}.tar.gz
Source1:    mls_client.proto
Source100:  mls-client.yaml
Source101:  mls-client-rpmlintrc
Patch0:     proto_not_from_git.patch
BuildRequires:  pkgconfig(openssl) >= 1.1.1
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(protobuf-lite)
BuildRequires:  pkgconfig(grpc)
BuildRequires:  pkgconfig(gflags)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  cmake(mlspp-config)

%description
%{summary}.

%if "%{?vendor}" == "chum"
Title: MLS Client
DeveloperName: Cisco Systems
DeveloperLogin: cisco
PackagedBy: nephros
Categories:
 - Utility
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

# proto_not_from_git.patch
%patch0 -p1
# >> setup
# << setup

%build
# >> build pre
# for SFOS 3.4, which has cmake 3.11.3.
# Then again, SFOS 3.4 does not have openssl 1.1 either so this is moot:
# sed -i 's/cmake_minimum_required(VERSION 3.12)/cmake_minimum_required(VERSION 3.11)/' CMakeLists.txt
pushd cmd/interop
# << build pre

%cmake . 

# >> build post
%make_build
popd
# << build post

%install
rm -rf %{buildroot}
# >> install pre
pushd cmd/interop
%make_install
popd
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%license LICENSE
%{_bindir}/%{name}_client
# >> files

# << files

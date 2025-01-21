Name:    rb-secor
Version: %{__version}
Release: %{__release}%{?dist}

License: GNU AGPLv3
URL: https://github.com/redBorder/rb-secor
Source0: %{name}-%{version}.tar.gz

BuildRequires: maven java-devel

Summary: Extension of secor service, to organize raw data in namespaces.   
Group:   Services/Persistence
Requires: java secor

%description
%{summary}

%global debug_package %{nil}

%prep
%setup -qn %{name}-%{version}

%build
mvn clean package

%install
mkdir -p %{buildroot}/var/secor/%{name}
install -D -m 644 target/rb-secor*-SNAPSHOT.jar %{buildroot}/var/secor/%{name}
install -D -m 644 resources/lib/* %{buildroot}/var/secor/lib/
install -D -m 644 resources/systemd/* %{buildroot}/usr/lib/systemd/system/
install -D -m 755 resources/scripts/* %{buildroot}/usr/lib/redborder/bin/

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root)
/var/secor/%{name}
/var/secor/lib
/usr/lib/systemd/system/*
/usr/lib/redborder/bin/*

%changelog
* Fri Jun 10 2016 Alberto Rodriguez <arodriguez@redborder.com> - 1.0.0-1
- first spec version
* Fri Jun 10 2016 Alberto Rodriguez <arodriguez@redborder.com> - 1.0.0-1
- first spec version

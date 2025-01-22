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
<<<<<<< HEAD
mkdir -p %{buildroot}/var/secor/
mkdir -p %{buildroot}/var/secor/lib
mkdir -p %{buildroot}/usr/lib/systemd/system/
mkdir -p %{buildroot}/usr/lib/redborder/bin/
install -D -m 644 target/rb-secor*-SNAPSHOT.jar %{buildroot}/var/secor/
install -D -m 644 resources/lib/* %{buildroot}/var/secor/lib/
install -D -m 644 resources/systemd/* %{buildroot}/usr/lib/systemd/system/
install -D -m 755 resources/scripts/*.sh %{buildroot}/usr/lib/redborder/bin/

%post
/bin/systemctl daemon-reload || :
=======
mkdir -p %{buildroot}/usr/lib/%{name}
install -D -m 644 target/rb-secor*-SNAPSHOT.jar %{buildroot}/usr/lib/%{name}
install -D -m 644 jets3t.properties %{buildroot}/etc/secor/jets3t.properties
>>>>>>> origin/development

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,root)
/usr/lib/redborder/bin/*
%defattr(644,root,root)
<<<<<<< HEAD
/var/secor/
/var/secor/lib
/usr/lib/systemd/system/*
=======
/usr/lib/%{name}
%config /etc/secor/jets3t.properties
>>>>>>> origin/development

%changelog
* Wen Jan 22 2025 Miguel Alvarez <malvarez@redborder.com> -
- Add secor and secor vault systemd files

* Fri Jun 10 2016 Alberto Rodriguez <arodriguez@redborder.com> - 1.0.0-1
- first spec version

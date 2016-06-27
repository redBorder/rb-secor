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

%prep
%setup -qn %{name}-%{version}

%build
mvn clean package

%install
mkdir -p %{buildroot}/usr/share/%{name}
install -D -m 644 target/rb-secor*-SNAPSHOT.jar %{buildroot}/usr/share/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root)
/usr/share/%{name}

%changelog
* Fri Jun 10 2016 Alberto Rodriguez <arodriguez@redborder.com> - 1.0.0-1
- first spec version

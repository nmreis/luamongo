Name:		luamongo
Version:	0.4
Release:	4%{?dist}
Summary:	Lua driver for MongoDB

License:	MIT
URL:		https://github.com/moai/luamongo
Source0:	%{name}-%{version}.tar.gz

BuildRequires: boost-devel
BuildRequires: boost-filesystem
BuildRequires: boost-thread
BuildRequires: lua52-devel
BuildRequires: libmongodb-devel
BuildRequires: libmongo-client-devel
Requires: lua52

%description
The current implementation does not give you raw access to the BSON objects. 
BSON objects are passed to the API using a Lua table or 
a JSON string representation. Every returned BSON document is 
fully marshalled to a Lua table.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
#make install DESTDIR=%{buildroot} INSTALL="install -p"
rm -f %{buildroot}/%{_libdir}/*.{a,la}
mkdir -p %{buildroot}/%{_libdir}/lua/5.2
cp mongo.so %{buildroot}/%{_libdir}/lua/5.2


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%{_libdir}/lua/5.2/mongo.so


%changelog
* Tue Jul 29 2014 FSCloud Release Engineering <nreis@wavecom.pt> - 0.4.4
- First version

%define upstream_name    Storable
%define upstream_version 2.21

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5

Summary:    Persistent data structure mechanism
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz


BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The Storable package brings persistence to your Perl data structures
containing SCALAR, ARRAY, HASH or REF objects, i.e. anything that can be
conveniently stored to disk and retrieved at a later time.

It can be used in the regular procedural way by calling 'store' with a
reference to the object to be stored, along with the file name where the
image should be written.

The routine returns 'undef' for I/O problems or other internal error, a
true value otherwise. Serious errors are propagated as a 'die' exception.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_mandir}/man3/*
%perl_vendorlib/*



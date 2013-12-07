%define modname	Storable
%define modver	2.30

Summary:	Persistent data structure mechanism
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	7
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AM/AMS/%{modname}-%{modver}.tar.gz
BuildRequires:	perl-devel

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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*


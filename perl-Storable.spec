%define upstream_name    Storable
%define upstream_version 2.30

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:    Persistent data structure mechanism
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/A/AM/AMS/%{upstream_name}-%{upstream_version}.tar.gz


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




%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.300.0-3mdv2012.0
+ Revision: 765656
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.300.0-2
+ Revision: 764168
- rebuilt for perl-5.14.x

* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.300.0-1
+ Revision: 690311
- update to new version 2.30

* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.290.0-1
+ Revision: 688827
- update to new version 2.29

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.250.0-2
+ Revision: 667311
- mass rebuild

* Sun Dec 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.250.0-1mdv2011.0
+ Revision: 623025
- new version
- update to new version 2.24

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 2.210.0-5mdv2011.0
+ Revision: 564580
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.210.0-4mdv2011.0
+ Revision: 556147
- rebuild for perl 5.12

* Sun Feb 28 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.210.0-3mdv2010.1
+ Revision: 512566
- Bump release

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 2.210.0-2mdv2010.0
+ Revision: 420985
- rebuild

* Thu Aug 20 2009 Jérôme Quelin <jquelin@mandriva.org> 2.210.0-1mdv2010.0
+ Revision: 418652
- update to 2.21

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 2.200.0-1mdv2010.0
+ Revision: 395248
- import perl-Storable


* Sun Jul 12 2009 cpan2dist 2.20-1mdv
- initial mdv release, generated with cpan2dist

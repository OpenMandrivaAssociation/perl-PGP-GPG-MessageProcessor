%define	module	PGP-GPG-MessageProcessor
%define	name	perl-%{module}
%define	version	0.4.5
%define	release	%mkrel 12

Name:		%{name}
Summary:	Perl module that supplies object methods for interacting with GnuPG
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
URL:		http://www.cpan.org/
Source:		%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:perl-devel
%endif
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildarch:	noarch

%description
This module provides an interface to the encryption/decryption/signing/
verifying methods of GNU Privacy Gaurd.  It does not provide keyring
manipulation.

%prep 
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING  MANIFEST NEWS  README  TODO
%{perl_vendorlib}/PGP/GPG/*
%_mandir/*/*


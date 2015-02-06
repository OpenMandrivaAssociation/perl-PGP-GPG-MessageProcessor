%define	module	PGP-GPG-MessageProcessor

Name:		perl-%{module}
Summary:	Perl module that supplies object methods for interacting with GnuPG
Version:	0.4.5
Release:	17
License:	GPL
Group:		Development/Perl
URL:		http://www.cpan.org/
Source:		%{module}-%{version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module provides an interface to the encryption/decryption/signing/
verifying methods of GNU Privacy Gaurd. It does not provide keyring
manipulation.

%prep 
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc COPYING  MANIFEST NEWS  README  TODO
%{perl_vendorlib}/PGP/GPG/*
%{_mandir}/*/*


%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.4.5-14mdv2010.0
+ Revision: 430527
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.4.5-13mdv2009.0
+ Revision: 258227
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.4.5-12mdv2009.0
+ Revision: 246286
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.4.5-10mdv2008.1
+ Revision: 136335
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 0.4.5-10mdv2008.0
+ Revision: 25177
- rebuild


* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.4.5-9mdk
- remove -q

* Fri Sep 10 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.4.5-8mdk
- rebuild

* Mon Aug 18 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.4.5-7mdk
- rebuild for new perl
- don't rm -rf $RPM_BUILD_ROOT in %%prep
- drop $RPM_OPT_FLAGS, noarch..
- use %%makeinstall_std macro
- cosmetics

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.4.5-6mdk
- rebuild for new auto{prov,req}

* Mon May 05 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.4.5-5mdk
- buildrequires

* Thu Aug 29 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.4.5-4mdk
- rebuild

* Thu Aug 23 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.4.5-3mdk
- rebuild

* Tue Sep 12 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.4.5-2mdk
- macros

* Wed Jun 21 2000 Vincent Danen <vdanen@linux-mandrake.com> 0.4.5-1mdk
- initial specfile
- bzip sources


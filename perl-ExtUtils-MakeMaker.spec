#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	ExtUtils
%define	pnam	MakeMaker
Summary:	ExtUtils::MakeMaker - create a module Makefile
Summary(pl):	ExtUtils::MakeMaker - tworzenie Makefile dla modu�u
Name:		perl-ExtUtils-MakeMaker
Version:	6.21
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	551c73ed52a36a93af8c305c71a554e5
Patch0:		%{name}-pm_to_blib_before_PERLRUNINST.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This utility is designed to write a Makefile for an extension module
from a Makefile.PL. It is based on the Makefile.SH model provided by
Andy Dougherty and the perl5-porters.

%description -l pl
To narz�dzie zosta�o zaprojektowane, aby tworzy� pliki Makefile dla
modu�u rozszerzenia z Makefile.PL. Jest oparte na modelu Makefile.SH
stworzonym przez Andy'ego Dougherty'ego i grup� perl5-porters.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# get rid of pod docuemntation
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/ExtUtils/MakeMaker/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes NOTES PATCHING README TODO
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/%{pdir}/*
%{_mandir}/man3/*
%{_mandir}/man1/*

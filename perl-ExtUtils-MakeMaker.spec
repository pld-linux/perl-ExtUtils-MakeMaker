#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	ExtUtils
%define	pnam	MakeMaker
Summary:	ExtUtils::MakeMaker - create a module Makefile
Summary(pl):	ExtUtils::MakeMaker - tworzenie Makefile dla modu³u
Name:		perl-ExtUtils-MakeMaker
Version:	6.17
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	983378d9e9a3ea73178ec3443f626048
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This utility is designed to write a Makefile for an extension module
from a Makefile.PL. It is based on the Makefile.SH model provided by
Andy Dougherty and the perl5-porters.

%description -l pl
To narzêdzie zosta³o zaprojektowane, aby tworzyæ pliki Makefile dla
modu³u rozszerzenia z Makefile.PL. Jest oparte na modelu Makefile.SH
stworzonym przez Andy'ego Dougherty'ego i grupê perl5-porters.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes NOTES PATCHING README TODO
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/%{pdir}/*
%{_mandir}/man3/*

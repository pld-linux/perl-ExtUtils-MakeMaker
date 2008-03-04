#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	ExtUtils
%define		pnam	MakeMaker
Summary:	ExtUtils::MakeMaker - create a module Makefile
Summary(pl.UTF-8):	ExtUtils::MakeMaker - tworzenie Makefile dla modułu
Name:		perl-ExtUtils-MakeMaker
Version:	6.44
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
# Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
Source0:	http://www.pobox.com/~schwern/src/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5a2480c2fcdada06b668f910b07509fe
Patch0:		%{name}-write-permissions.patch
URL:		http://search.cpan.org/dist/ExtUtils-MakeMaker/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This utility is designed to write a Makefile for an extension module
from a Makefile.PL. It is based on the Makefile.SH model provided by
Andy Dougherty and the perl5-porters.

%description -l pl.UTF-8
To narzędzie zostało zaprojektowane, aby tworzyć pliki Makefile dla
modułu rozszerzenia z Makefile.PL. Jest oparte na modelu Makefile.SH
stworzonym przez Andy'ego Dougherty'ego i grupę perl5-porters.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

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

#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
#
%define		pdir	ExtUtils
%define		pnam	MakeMaker
Summary:	ExtUtils::MakeMaker - create a module Makefile
Summary(pl.UTF-8):	ExtUtils::MakeMaker - tworzenie Makefile dla modułu
Name:		perl-ExtUtils-MakeMaker
Version:	6.62
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2ae291030c52999b5672b2a502eab195
Patch0:		%{name}-write-permissions.patch
URL:		http://search.cpan.org/dist/ExtUtils-MakeMaker/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.50
BuildRequires:	perl(File::Spec) >= 0.80
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
# the following are needed to avoid installation of bundled modules
BuildRequires:	perl-CPAN-Meta >= 2.112150
BuildRequires:	perl-CPAN-Meta-YAML >= 0.003
BuildRequires:	perl-ExtUtils-Command >= 1.16
BuildRequires:	perl-ExtUtils-Install >= 1.52
BuildRequires:	perl-ExtUtils-Manifest >= 1.58
BuildRequires:	perl-File-Copy-Recursive >= 0.38
BuildRequires:	perl-File-Temp >= 0.22
BuildRequires:	perl-JSON-PP >= 2.27104
BuildRequires:	perl-Parse-CPAN-Meta >= 1.4401
BuildRequires:	perl-Scalar-List-Utils >= 1.23
BuildRequires:	perl-Version-Requirements >= 0.101020
BuildRequires:	perl-version >= 0.88
%if %{with tests}
BuildRequires:	perl-Test-Harness >= 2.00
%endif
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

find inc -name '*.orig' | xargs -r %{__rm}

# perl >= 5.8 is assumed, so this module is useless
%{__rm} -r bundled/JSON-PP-Compat5006

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
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/ExtUtils/MakeMaker/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes NOTES PATCHING README TODO
%attr(755,root,root) %{_bindir}/instmodsh
%{perl_vendorlib}/ExtUtils/Command
%{perl_vendorlib}/ExtUtils/Liblist.pm
%{perl_vendorlib}/ExtUtils/Liblist
%{perl_vendorlib}/ExtUtils/MM.pm
%{perl_vendorlib}/ExtUtils/MM_*.pm
%{perl_vendorlib}/ExtUtils/MY.pm
%{perl_vendorlib}/ExtUtils/MakeMaker.pm
%{perl_vendorlib}/ExtUtils/MakeMaker
%{perl_vendorlib}/ExtUtils/Mkbootstrap.pm
%{perl_vendorlib}/ExtUtils/Mksymlists.pm
%{perl_vendorlib}/ExtUtils/testlib.pm
%{_mandir}/man1/instmodsh.1p*
%{_mandir}/man3/ExtUtils::Command::*.3pm*
%{_mandir}/man3/ExtUtils::Liblist.3pm*
%{_mandir}/man3/ExtUtils::MM*.3pm*
%{_mandir}/man3/ExtUtils::MY.3pm*
%{_mandir}/man3/ExtUtils::MakeMaker*.3pm*
%{_mandir}/man3/ExtUtils::Mkbootstrap.3pm*
%{_mandir}/man3/ExtUtils::Mksymlists.3pm*
%{_mandir}/man3/ExtUtils::testlib.3pm*

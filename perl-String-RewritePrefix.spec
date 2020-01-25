#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	String
%define	pnam	RewritePrefix
Summary:	String::RewritePrefix - rewrite strings based on a set of known prefixes
Summary(pl.UTF-8):	String::RewritePrefix - przepisz łańcucy znaków w oparciu o zbiór znanych prefiksów
Name:		perl-String-RewritePrefix
Version:	0.007
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7135a69bd8cf74cf17dba857b2372d16
URL:		http://search.cpan.org/dist/String-RewritePrefix/
BuildRequires:	perl-Sub-Exporter
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl library to rewrite strings based on string prefixes.

%description -l pl.UTF-8
Biblioteka Perla do przepisywania lancuow na bazie prefiksow.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/String/*.pm
%{_mandir}/man3/*

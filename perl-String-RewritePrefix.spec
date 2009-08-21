#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	RewritePrefix
Summary:	String::RewritePrefix - rewrite strings based on a set of known prefixes
Summary(pl.UTF-8):	String::RewritePrefix - przepisz łańcucy znaków w oparciu o zbiór znanych prefiksów
Name:		perl-String-RewritePrefix
Version:	0.004
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	27aeb4769fb047651b996bcc12aeabca
URL:		http://search.cpan.org/dist/String-RewritePrefix/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

# %description -l pl.UTF-8
# TODO

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
%doc Changes INSTALL README
%{perl_vendorlib}/String/*.pm
%{_mandir}/man3/*

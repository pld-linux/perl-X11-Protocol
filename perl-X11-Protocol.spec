#
# Conditional build:
%bcond_with	tests	# perform "make test" (runs xmms)
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	X11
%define	pnam	Protocol
Summary:	Perl module for the X Window System protocol
Summary(pl):	Modu³ Perla obs³uguj±cy protokó³ X Window System
Name:		perl-%{pdir}-%{pnam}
Version:	0.53
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4021756e9d7f2051ff63a1062a9512eb
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl module with bindings for XLib library.

%description -l pl
Modu³ Perla umo¿liwiaj±cy korzystanie z biblioteki XLib.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc MANIFEST README Todo eg/
%dir %{perl_vendorlib}/X11
%{perl_vendorlib}/X11/*.pm
%{perl_vendorlib}/X11/Protocol
%{_mandir}/man3/*

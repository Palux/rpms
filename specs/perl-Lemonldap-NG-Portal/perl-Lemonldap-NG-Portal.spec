# $Id$
# Authority: dag
# Upstream: Xavier Guimard <x,guimard$free,fr>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lemonldap-NG-Portal

Summary: The authentication portal part of Lemonldap::NG Web-SSO
Name: perl-Lemonldap-NG-Portal
Version: 0.87
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lemonldap-NG-Portal/

Source: http://www.cpan.org/modules/by-module/Lemonldap/Lemonldap-NG-Portal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
The authentication portal part of Lemonldap::NG Web-SSO.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find example/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
#doc example/
%doc %{_mandir}/man3/Lemonldap::NG::Portal.3pm*
%doc %{_mandir}/man3/Lemonldap::NG::Portal::*.3pm*
%{perl_vendorlib}/auto/Lemonldap/
%dir %{perl_vendorlib}/Lemonldap/
%dir %{perl_vendorlib}/Lemonldap/NG/
%{perl_vendorlib}/Lemonldap/NG/Portal/
%{perl_vendorlib}/Lemonldap/NG/Portal.pm

%changelog
* Fri Jul 24 2009 Dag Wieers <dag@wieers.com> - 0.87-1
- Initial package. (using DAR)

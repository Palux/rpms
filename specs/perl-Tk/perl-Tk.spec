# $Id$

# Authority: dries
# Upstream: Nick Ing-Simmons <nick$ing-simmons,net>

%define real_name Tk
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Object Oriented Tk extension for Perl
Name: perl-Tk
Version: 804.027
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tk/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/N/NI/NI-S/Tk-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
Provides: perl(Tk::LabRadio), perl(Tk::TextReindex)

%description
This module contains an object oriented Tk extension for Perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__perl} -pi -e 's|/bin/perl|%{_bindir}/perl|g' %{buildroot}%{perl_vendorarch}/Tk/reindex.pl
%{__perl} -pi -e 's|/usr/local/bin/perl|%{_bindir}/perl|g' \
	%{buildroot}%{perl_vendorarch}/Tk/demos/widtrib/plop.pl \
	%{buildroot}%{perl_vendorarch}/Tk/demos/widtrib/npuz.pl \
	%{buildroot}%{perl_vendorarch}/Tk/pTk/mkVFunc \
	%{buildroot}%{perl_vendorarch}/Tk/pTk/Tcl-pTk \
	%{buildroot}%{perl_vendorarch}/Tk/Text.pod

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_bindir}/gedi
%{_bindir}/ptked
%{_bindir}/ptksh
%{_bindir}/tkjpeg
%{_bindir}/widget
%{perl_vendorarch}/Tie/Watch.pm
%{perl_vendorarch}/Tk.pm
%{perl_vendorarch}/Tk.pod
%{perl_vendorarch}/Tk
%{perl_vendorarch}/auto/Tk
%{perl_vendorarch}/fix_4_os2.pl
%exclude %{perl_archlib}/perllocal.pod

%changelog
* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 804.027-1
- Initial package.

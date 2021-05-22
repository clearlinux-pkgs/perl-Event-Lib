#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Event-Lib
Version  : 1.03
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/V/VP/VPARSEVAL/Event-Lib-1.03.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/V/VP/VPARSEVAL/Event-Lib-1.03.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Event-Lib-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : pkgconfig(libevent)
Patch1: buildfix.patch

%description
Event-Lib version 1.03
=========================
This module is a Perl wrapper around libevent(3) as available from
<http://www.monkey.org/~provos/libevent/>.  It allows to execute a function
whenever a given event on a filehandle happens, a timeout occurs or a signal is
received.

%package dev
Summary: dev components for the perl-Event-Lib package.
Group: Development
Provides: perl-Event-Lib-devel = %{version}-%{release}
Requires: perl-Event-Lib = %{version}-%{release}

%description dev
dev components for the perl-Event-Lib package.


%package perl
Summary: perl components for the perl-Event-Lib package.
Group: Default
Requires: perl-Event-Lib = %{version}-%{release}

%description perl
perl components for the perl-Event-Lib package.


%prep
%setup -q -n Event-Lib-1.03
cd %{_builddir}/Event-Lib-1.03
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Event::Lib.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Event/Lib.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Event/Lib/Lib.so

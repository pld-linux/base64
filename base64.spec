Summary:	Encode and decode base64 files
Summary(pl):	(De)szyfruje pliki base64
Name:		base64
Version:	1.3
Release:	1
License:	Public Domain
Group:		Applications
Source0:	http://www.fourmilab.ch/webtools/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	66d81725ba4d03227af2ce3792e50d5d
URL:		http://www.fourmilab.ch/webtools/base64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
base64 is a command line utility which encodes and decodes files in
this format. It can be used within a pipeline as an encoding or
decoding filter, and is most commonly used in this manner as part of
an automated mail processing system.

%description -l pl
base64 to narzêdzie konsolowe s³u¿±ce do szyfrowania i deszyfrowania
plików w tym formacie. Mo¿e byæ u¿ywane w potokach jako filtr
(de)szyfruj±cy i jest w ten sposób u¿ywany w systemach automatycznego
przetwarzania poczty.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_pixmapsdir}}

install base64 $RPM_BUILD_ROOT%{_bindir}
install base64.1 $RPM_BUILD_ROOT%{_mandir}/man1
install b64.gif $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README index.html rfc1341* base64.pdf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_pixmapsdir}/*

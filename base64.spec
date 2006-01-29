Summary:	Encode and decode base64 files
Summary(pl):	Kodowanie i dekodowanie plik�w base64
Name:		base64
Version:	1.4
Release:	1
License:	Public Domain
Group:		Applications
Source0:	http://www.fourmilab.ch/webtools/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	77f0ff05296e1bd446ff02cea279309a
URL:		http://www.fourmilab.ch/webtools/base64/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
base64 is a command line utility which encodes and decodes files in
this format. It can be used within a pipeline as an encoding or
decoding filter, and is most commonly used in this manner as part of
an automated mail processing system.

%description -l pl
base64 to narz�dzie konsolowe s�u��ce do kodowania i dekodowania
plik�w w tym formacie. Mo�e by� u�ywane w potokach jako filtr
(de)koduj�cy i jest zwykle w ten spos�b u�ywane w systemach
automatycznego przetwarzania poczty.

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
install b64.png	$RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README index.html rfc1341* base64.pdf log.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_pixmapsdir}/*
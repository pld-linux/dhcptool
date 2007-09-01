Summary:	dhcptool - an utility to generate and transmit custom DHCP/BOOTP packets
Summary(pl.UTF-8):	dhcptool - narzędzie do generowania i przesyłania własnych pakietów DHCP/BOOTP
Name:		dhcptool
Version:	0.8b
Release:	1
License:	BSD
Group:		Networking/Utilities
Source0:	http://www.gatorhole.com/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	96f9ee1cc96631d52972a992af725f7c
URL:		http://gatorhole.com/index.php?product=dhcp
BuildRequires:	libnet-devel
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DHCPTool is a command-line utility used to e.g. test DHCP servers or
DHCP relay agents. It can generate almost any kind of DHCP packet,
and the idea is to facilitate simulation of e.g. broken DHCP clients
to see how well servers handle them and/or to detect stability bugs
in any software that parses DHCP messages.

%description -l pl.UTF-8
DHCPTool to obsługiwane z linii poleceń narzędzei służące np. do
testowania serwerów DHCP lub agentów przekazujących DHCP. Potrafi
wygenerować prawie każdy rodzaj pakietu DHCP, mając na celu ułatwienie
symulacji np. wadliwych klientów DHCP, aby sprawdzić, jak dobrze
serwery są w stanie je obsłużyć, albo wykryć błędy stabilności w
dowolnym kodzie analizującym komunikaty DHCP.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -D dhcptool   $RPM_BUILD_ROOT%{_bindir}/dhcptool
install -D dhcptool.1 $RPM_BUILD_ROOT%{_mandir}/man1/dhcptool.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

Summary:	Configurable mixer for ALSA
Summary(pl):	Konfigurowalny mikser dla ALSA
Name:		qamix
Version:	0.0.4
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	ftp://ftp.suse.com/pub/people/mana/%{name}-%{version}.tar.bz2
# Source0-md5:	81d316126b8735052164203eac84c0b8
Source1:	%{name}.desktop
Patch0:		%{name}-paths_and_optflags.patch
URL:		http://www.suse.de/~mana/kalsatools.html
BuildRequires:	alsa-lib-devel >= 0.9.0
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QAMix is a configurable mixer for ALSA. The GUI description is defined
in an XML file. Default interfaces for standard AC 97 cards and
Soundblaster Live! are provided. QAMix can be controlled via MIDI.
Any number of MIDI events can be bound to any mixer control.

%description -l pl
QAMix jest konfigurowalnym mikserem dla ALSA. Opis GUI jest
zdefiniowany w pliku XML. Predefiniowane ustawienia dla standardu
AC 97 i kart Soundblaster Live! s± dostarczone wraz z pakietem.
QAMix mo¿e byæ kontrolowany poprzez MIDI. Dowolna liczba zdarzeñ
MIDI mo¿e byæ przydzielona do jakichkolwiek kontrolerów miksera.

%prep
%setup -q 
%patch0 -p1

%build
%{__make} \
	-f make_qamix \
	OPTFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/qamix,%{_applnkdir}/Multimedia}

install -c %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia
install -c qamix $RPM_BUILD_ROOT%{_bindir}
install -c *.xml $RPM_BUILD_ROOT%{_datadir}/qamix/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README THANKS
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.xml
%{_applnkdir}/Multimedia/%{name}.desktop

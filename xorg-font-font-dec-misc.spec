Summary:	DEC bitmap fonts
Summary(pl.UTF-8):	Fonty bitmapowe DEC
Name:		xorg-font-font-dec-misc
Version:	1.0.0
Release:	2
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-dec-misc-%{version}.tar.bz2
# Source0-md5:	284e554db1c64fb7580a06df01444a2b
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DEC cursor and session bitmap fonts.

%description -l pl.UTF-8
Fonty bitmapowe DEC cursor i session.

%prep
%setup -q -n font-dec-misc-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-fontdir=%{_fontsdir}/misc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_fontsdir}/misc/dec*.pcf.gz

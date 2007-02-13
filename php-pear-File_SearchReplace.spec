%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	SearchReplace
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - performs search and replace routines
Summary(pl.UTF-8):	%{_pearname} - metody przeszukiwania i zamieniania
Name:		php-pear-%{_pearname}
Version:	1.1.1
Release:	1
Epoch:		0
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	527285477680226e4e010fe1d9981422
URL:		http://pear.php.net/package/File_SearchReplace/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides various functions to perform search/replace on files.
Preg/Ereg regex supported along with faster but more basic str_replace
routine.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa zawiera różne funkcje do wyszukiwania i zamiany ciągów w
plikach. Wyrażenia preg/ereg są obsługiwane poprzez szybką, ale
bardziej podstawową funkcję str_replace.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*

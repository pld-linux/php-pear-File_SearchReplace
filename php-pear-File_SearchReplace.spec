%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	SearchReplace
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - performs search and replace routines
Summary(pl):	%{_pearname} - metody przeszukiwania i zamieniania
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	2
Epoch:		0
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	609d56e86c8875e17bf19ea1595dc001
URL:		http://pear.php.net/package/File_SearchReplace/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides various functions to perform search/replace on files.
Preg/Ereg regex supported along with faster but more basic str_replace
routine.

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa zawiera ró¿ne funkcje do wyszukiwania i zamiany ci±gów w
plikach. Wyra¿enia preg/ereg s± obs³ugiwane poprzez szybk±, ale
bardziej podstawow± funkcjê str_replace.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
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

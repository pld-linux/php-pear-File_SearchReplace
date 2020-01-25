%define		_status		stable
%define		_pearname	File_SearchReplace
Summary:	%{_pearname} - performs search and replace routines
Summary(pl.UTF-8):	%{_pearname} - metody przeszukiwania i zamieniania
Name:		php-pear-%{_pearname}
Version:	1.1.4
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a5f817ede450df7f8adf34d0a714a693
URL:		http://pear.php.net/package/File_SearchReplace/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-File_SearchReplace-tests
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
%{php_pear_dir}/File/SearchReplace.php

%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	SearchReplace
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - performs search and replace routines
Summary(pl):	%{_pearname} - metody przeszukiwania i zamieniania
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	2
License:	BSD
Group:		Development/Languages/PHP
# Source0-md5:	bbf1709f6d340ac602f39a0aaeb18492
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/File_SearchReplace/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
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

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php

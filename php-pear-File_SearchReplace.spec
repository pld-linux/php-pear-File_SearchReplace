%include	/usr/lib/rpm/macros.php
%define         _class          File
%define         _subclass       SearchReplace
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Performs search and replace routines
Summary(pl):	%{_class}_%{_subclass} - Metody przeszukiwania i zamieniania
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
BuildRequires:	rpm-php-pearprov
URL:		http://pear.php.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides various functions to perform search/replace on files.
Preg/Ereg regex supported along with faster but more basic str_replace
routine.

%description -l pl

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
cd %{_pearname}-%{version}

install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install *.php			$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php

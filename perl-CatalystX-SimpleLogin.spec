%define upstream_name    CatalystX-SimpleLogin
%define upstream_version 0.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Redirect
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CatalystX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst::Action::REST)
BuildRequires:	perl(Catalyst::Action::RenderView)
BuildRequires:	perl(Catalyst::ActionRole::ACL)
BuildRequires:	perl(Catalyst::Controller::ActionRole)
BuildRequires:	perl(Catalyst::Plugin::Authentication)
BuildRequires:	perl(Catalyst::Plugin::Session)
BuildRequires:	perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires:	perl(Catalyst::Plugin::Session::Store::File)
BuildRequires:	perl(Catalyst::Runtime)
BuildRequires:	perl(Catalyst::View::TT)
BuildRequires:	perl(CatalystX::Component::Traits)
BuildRequires:	perl(CatalystX::InjectComponent)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(HTML::FormHandler)
BuildRequires:	perl(HTTP::Request::Common)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(MooseX::MethodAttributes)
BuildRequires:	perl(MooseX::RelatedClassRoles)
BuildRequires:	perl(MooseX::Types)
BuildRequires:	perl(MooseX::Types::Common)
BuildRequires:	perl(SQL::Translator)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

%description
CatalystX::SimpleLogin is an application class role which will inject a
controller which is an instance of the
CatalystX::SimpleLogin::Controller::Login manpage into your application.
This provides a simple login and logout page with the adition of only one
line of code and one template to your application.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*


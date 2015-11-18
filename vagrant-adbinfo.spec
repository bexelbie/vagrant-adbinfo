# Generated from vagrant-adbinfo-0.0.4.gem by gem2rpm -*- rpm-spec -*-
%global vagrant_plugin_name vagrant-adbinfo

Name: %{vagrant_plugin_name}
Version: 0.0.5
Release: 2%{?dist}
Summary: Vagrant plugin that provides the IP address:port and TLS certificate file location for a Docker daemon
Group: Development/Languages
License: GPLv2 
URL: https://github.com/bexelbie/vagrant-adbinfo
Source0: https://rubygems.org/gems/%{vagrant_plugin_name}-%{version}.gem
Requires(posttrans): vagrant
Requires(preun): vagrant
Requires: vagrant
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby 
BuildRequires: vagrant
BuildArch: noarch
Provides: vagrant(%{vagrant_plugin_name}) = %{version}

%description
Vagrant plugin that provides the IP address:port and TLS certificate file
location for a Docker daemon.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{vagrant_plugin_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{vagrant_plugin_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{vagrant_plugin_name}.gemspec

# %%vagrant_plugin_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%vagrant_plugin_install

%install
mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -a .%{vagrant_plugin_dir}/* \
        %{buildroot}%{vagrant_plugin_dir}/

# Run the test suite
%check
pushd .%{vagrant_plugin_instdir}

popd

%posttrans
%vagrant_plugin_register %{vagrant_plugin_name}

%preun
%vagrant_plugin_unregister %{vagrant_plugin_name}

%files
%dir %{vagrant_plugin_instdir}
%exclude %{vagrant_plugin_instdir}/.gitignore
%{vagrant_plugin_libdir}
%exclude %{vagrant_plugin_cache}
%{vagrant_plugin_spec}

%files doc
%doc %{vagrant_plugin_docdir}
%{vagrant_plugin_instdir}/Gemfile
%doc %{vagrant_plugin_instdir}/README.md
%{vagrant_plugin_instdir}/Rakefile
%{vagrant_plugin_instdir}/Vagrantfile
%{vagrant_plugin_instdir}/vagrant-adbinfo.gemspec

%changelog
* Thu Nov 18 2015 Navid Shaikh - 0.0.5-2
- Removes shadow-utils from Requires

* Tue Nov 17 2015 Navid Shaikh - 0.0.5-1
- vagrant-adbinfo#17: adbinfo format should be windows compatible 
- vagrant-adbinfo#18: adbinfo should be possible to evaluate in shell

* Thu Nov 12 2015 Navid Shaikh - 0.0.4-1
- Initial package

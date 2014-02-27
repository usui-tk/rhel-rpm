%global major_version 2
%global minor_version 1
%global teeny_version 1
%global patch_level   76

%global major_minor_version %{major_version}.%{minor_version}

%global ruby_version %{major_minor_version}.%{teeny_version}
%global ruby_version_patch_level %{major_minor_version}.%{teeny_version}.%{patch_level}
%global ruby_abi %{major_minor_version}

%global ruby_archive %{pkg_name}-%{ruby_version}-p%{patch_level}

%global ruby_libdir %{_datadir}/%{pkg_name}
%global ruby_libarchdir %{_libdir}/%{pkg_name}

# This is the local lib/arch and should not be used for packaging.
%global ruby_sitedir site_ruby
%global ruby_sitelibdir %{_prefix}/local/share/ruby/%{ruby_sitedir}
%global ruby_sitearchdir %{_prefix}/local/%{_lib}/ruby/%{ruby_sitedir}

# This is the general location for libs/archs compatible with all
# or most of the Ruby versions available in the Fedora repositories.
%global ruby_vendordir vendor_ruby
%global ruby_vendorlibdir %{_datadir}/ruby/%{ruby_vendordir}
%global ruby_vendorarchdir %{_libdir}/ruby/%{ruby_vendordir}

Summary:        An interpreter of object-oriented scripting language
Name:           ruby
Version:        %{ruby_version_patch_level}
Release:        1%{?dist}
Group:          Development/Languages
License:        (Ruby or BSD) and Public Domain
URL:            http://www.ruby-lang.org/
Source0:        http://cache.ruby-lang.org/pub/%{name}/%{major_minor_version}/%{name}-%{ruby_version}.tar.gz
#Source0:       http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.0.tar.gz
#Source0:       http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.1.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  byacc
BuildRequires:  curl-devel
BuildRequires:  db4-devel
BuildRequires:  gcc
BuildRequires:  gdbm
BuildRequires:  gdbm-devel
BuildRequires:  glibc-devel
BuildRequires:  libffi
BuildRequires:  libffi-devel
BuildRequires:  libyaml
BuildRequires:  libyaml-devel
BuildRequires:  make
BuildRequires:  ncurses
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  readline
BuildRequires:  readline-devel
BuildRequires:  rpm-build
BuildRequires:  rpmdevtools
BuildRequires:  tcl-devel
BuildRequires:  unzip
BuildRequires:  zlib-devel

Provides:  ruby(abi) = 2.1
Provides:  ruby-irb
Provides:  ruby-rdoc
Provides:  ruby-libs
Provides:  ruby-devel
Provides:  rubygems

Obsoletes:  ruby
Obsoletes:  ruby-libs
Obsoletes:  ruby-irb
Obsoletes:  ruby-rdoc
Obsoletes:  ruby-devel
Obsoletes:  rubygems

Requires: epel-release
Requires: libyaml

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

%prep
%setup -n ruby-%{ruby_version}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"

%configure \
  --enable-shared \
  --disable-rpath \
  --without-X11 \
  --without-tk \
  --includedir=%{_includedir}/ruby \
  --libdir=%{_libdir}

make %{?_smp_mflags}

%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT

#we don't want to keep the src directory
rm -rf $RPM_BUILD_ROOT/usr/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}
%{_includedir}
%{_datadir}
%{_libdir}

%changelog
* Thu Feb 27 2014 Takayuki Usui <usui.takayuki@po.ntts.co.jp> - 2.1.1
- Updating with minor release of Ruby

* Thu Feb 2 2014 Takayuki Usui <usui.takayuki@po.ntts.co.jp> - 2.1.0
- Initial spec to replace system Ruby with 2.1.0-p0


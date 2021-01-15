#
# spec file for package gnu-cobol-sql
#

%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          gnu-cobol-sql
Summary:       ESQL for ODBC for GnuCobol/OpenCOBOL
Version:       2.0
Release:       0
License:       GPL-3.0-only and LGPL-3.0-only
Group:         Productivity/Databases/Tools
Source:        http://kiska.net/opencobol/esql/%{name}-%{version}.tar.gz
URL:           http://kiska.net/opencobol/esql/
PreReq:        /usr/bin/grep
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: unixODBC-devel
BuildRoot:     %{buildroot}
Requires: unixODBC

%description
This package contains ESQL Preprocessor and Runtime for ODBC for GnuCobol/OpenCOBOL.

%define lib_name libocsql2

%package -n %{lib_name}
Summary:        Shared library from gnu-cobol-sql
Group:          Productivity/Databases/Tools
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n %{lib_name}
This package holds the shared library of gnu-cobol-sql.

%package devel
Summary:        Development package for gnu-cobol-sql
Group:          Productivity/Databases/Tools
Requires:       %{lib_name} = %{version}

%description devel
This package contains the files needed to compile programs that use
the gnu-cobol-sql library.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --enable-static=no --with-multidb --prefix=%{directory} --libdir=%{directory}/%{_lib}
make 

%install
make DESTDIR=%{buildroot} install
rm -f %buildroot%_libdir/*.la

%postun -n %{lib_name} -p /sbin/ldconfig

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{directory}/bin/esqlOC

%files -n %{lib_name}
%{directory}/%{_lib}/libocsql.so.2
%{directory}/%{_lib}/libocsql.so.2.0.0

%files devel
%doc README AUTHORS ChangeLog COPYING COPYING.LESSER
%{directory}/%{_lib}/libocsql.so

Name:           nipy-data
Version:        0.2
Release:        1%{?dist}
Summary:        Test data and brain templates for nipy

License:        BSD
URL:            http://nipy.org/nipy/
Source0:        http://nipy.org/data-packages/nipy-data-%{version}.tar.gz
Source1:        http://nipy.org/data-packages/nipy-templates-%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%prep
%setup -q -c -T -b 0 -b 1

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/nipy/nipy/
for i in data templates
do
  cp -a nipy-$i-%{version}/$i/ %{buildroot}%{_datadir}/nipy/nipy/
  cp -a nipy-$i-%{version}/README.txt ./README-$i.txt
done

%files
%doc README-data.txt README-templates.txt
%{_datadir}/nipy/

%changelog
* Sun Nov 01 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.2-1
- Initial package

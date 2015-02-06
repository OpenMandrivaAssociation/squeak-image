Name:		squeak-image
Version:	4.1
Release:	2
Summary:	The image files for Squeak

Group:		Development/Other
License:	MIT
URL:		http://www.squeak.org
Source0:	http://ftp.squeak.org/%{version}/Squeak%{version}.zip
Source1:	http://ftp.squeak.org/sources_files/SqueakV41.sources.gz
Source2:	http://ftp.squeak.org/4.1/LICENSE
Source3:	squeak-image-doc.html
BuildRoot:	%{_tmppath}/%{name}-buildroot

Requires:	squeak-vm >= 4.0.3

BuildArch:	noarch


%description
This is the standard Squeak image as distributed by sqeak.org.
The Squeak image is split into three interdependent parts,
the .image file, the .changes file, and the .sources file.

%prep
%setup -q -c %{name}-%{version}
cp -p %{SOURCE2} %{SOURCE3} .

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/squeak
cp Squeak%{version}.image %{buildroot}%{_datadir}/squeak
cp Squeak%{version}.changes %{buildroot}%{_datadir}/squeak
zcat %{SOURCE1} >%{buildroot}%{_datadir}/squeak/SqueakV41.sources
cd %{buildroot}%{_datadir}/squeak
gzip Squeak%{version}.image
gzip Squeak%{version}.changes
ln -sf Squeak%{version}.image.gz squeak.image.gz
ln -sf Squeak%{version}.changes.gz squeak.changes.gz

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc squeak-image-doc.html
%doc LICENSE
%{_datadir}/squeak/*


%changelog
* Sat Oct 09 2010 Paulo Andrade <pcpa@mandriva.com.br> 4.1-1mdv2011.0
+ Revision: 584298
- Update to latest upstream release

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 3.10.2.7179-2mdv2010.0
+ Revision: 445209
- rebuild

* Fri Mar 06 2009 Jérôme Soyer <saispo@mandriva.org> 3.10.2.7179-1mdv2009.1
+ Revision: 349746
- New upstream release

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 3.9-4mdv2009.0
+ Revision: 260989
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 3.9-3mdv2009.0
+ Revision: 253076
- rebuild

* Sun Jan 06 2008 Jérôme Soyer <saispo@mandriva.org> 3.9-1mdv2008.1
+ Revision: 146063
- import squeak-image



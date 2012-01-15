Name:		squeak-image
Version:	4.1
Release:	%mkrel 4
Summary:	The image files for Squeak

Group:		Development/Other
License:	MIT
URL:		http://www.squeak.org
Source0:	http://ftp.squeak.org/%{version}/Squeak%{version}.zip
Source1:	http://ftp.squeak.org/sources_files/SqueakV41.sources.gz
Source2:	http://ftp.squeak.org/4.1/LICENSE
Source3:	squeak-image-doc.html
Source4:	Squeak4.1-pt_BR.changes.gz
Source5:	Squeak4.1-pt_BR.image.gz
BuildRoot:	%{_tmppath}/%{name}-buildroot

Requires:	squeak-vm >= 4.0.3

BuildArch:	noarch

#-----------------------------------------------------------------------
%description
This is the standard Squeak image as distributed by squeak.org.
The Squeak image is split into three interdependent parts,
the .image file, the .changes file, and the .sources file.

#-----------------------------------------------------------------------
%package	pt_BR
Summary:        Customized squeak image for pt_BR
Group:          Development/Other
Requires:       squeak-image = %{version}-%{release}

%description	pt_BR
Customized squeak image for pt_BR

#-----------------------------------------------------------------------
%prep
%setup -q -c %{name}-%{version}
cp -p %{SOURCE2} %{SOURCE3} .

#-----------------------------------------------------------------------
%build

#-----------------------------------------------------------------------
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
cp -p %{SOURCE4} %{SOURCE5} %{buildroot}%{_datadir}/squeak

#-----------------------------------------------------------------------
%clean
rm -rf %{buildroot}

#-----------------------------------------------------------------------
%files
%defattr(-,root,root,-)
%doc squeak-image-doc.html
%doc LICENSE
%dir %{_datadir}/squeak
%{_datadir}/squeak/Squeak4.1.changes.gz
%{_datadir}/squeak/Squeak4.1.image.gz
%ghost %{_datadir}/squeak/squeak.changes.gz
%ghost %{_datadir}/squeak/squeak.image.gz
%{_datadir}/squeak/SqueakV41.sources

#-----------------------------------------------------------------------
%post pt_BR
pushd %{_datadir}/squeak
    ln -sf Squeak%{version}-pt_BR.image.gz squeak.image.gz
    ln -sf Squeak%{version}-pt_BR.changes.gz squeak.changes.gz
popd

%postun pt_BR
if [ "$1" = "0" ]; then
    pushd %{_datadir}/squeak
	ln -sf Squeak%{version}.image.gz squeak.image.gz
	ln -sf Squeak%{version}.changes.gz squeak.changes.gz
    popd
fi

#-----------------------------------------------------------------------
%files		pt_BR
%defattr(-,root,root,-)
%{_datadir}/squeak/Squeak4.1-pt_BR.changes.gz
%{_datadir}/squeak/Squeak4.1-pt_BR.image.gz

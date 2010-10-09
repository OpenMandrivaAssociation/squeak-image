Name:		squeak-image
Version:	4.1
Release:	%mkrel 1
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

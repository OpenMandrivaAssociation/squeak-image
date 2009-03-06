%define image_major 3.10
%define image_ver %{image_major}.2
%define image_rel 7179

Name:           squeak-image
Version:        %{image_ver}.%{image_rel}
Release:        %mkrel 1
Summary:        The image files for Squeak

Group:          Development/Other
License:        MIT
URL:            http://www.squeak.org
Source0:        http://ftp.squeak.org/%{image_major}/Squeak%{image_ver}-%{image_rel}-basic.zip
Source1:        http://ftp.squeak.org/sources_files/SqueakV39.sources.gz
Source2:        squeak-image-doc.html
BuildRoot:      %{_tmppath}/%{name}-buildroot

Requires:       squeak-vm >= 3.7

BuildArch:      noarch


%description
This is the standard Squeak image as distributed by sqeak.org.
The Squeak image is split into three interdependent parts,
the .image file, the .changes file, and the .sources file.

%prep
%setup -q -c %{name}-%{version}
cp -p %SOURCE2 .

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/squeak
cp Squeak%{image_ver}-%{image_rel}-basic.image %{buildroot}%{_datadir}/squeak
cp Squeak%{image_ver}-%{image_rel}-basic.changes %{buildroot}%{_datadir}/squeak
zcat %{SOURCE1} >%{buildroot}%{_datadir}/squeak/SqueakV39.sources
cd %{buildroot}%{_datadir}/squeak
gzip Squeak%{image_ver}-%{image_rel}-basic.image
gzip Squeak%{image_ver}-%{image_rel}-basic.changes
ln -sf Squeak%{image_ver}-%{image_rel}-basic.image.gz squeak.image.gz
ln -sf Squeak%{image_ver}-%{image_rel}-basic.changes.gz squeak.changes.gz

# inisqueak is looking for SqueakV3.sources (not V39), create this for it
cd %{buildroot}%{_datadir}/squeak/
ln -s SqueakV39.sources SqueakV3.sources


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc squeak-image-doc.html
%{_datadir}/squeak/*

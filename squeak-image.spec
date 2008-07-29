%define major 7067
%define origin final

Summary:       Squeak Image
Name:          squeak-image
Version:       3.9
Release:       %mkrel 3
License:       Free with restrictions (http://www.squeak.org/download/license.html)
Group:         Development/Other
Source0:       ftp://st.cs.uiuc.edu/Smalltalk/Squeak/%version/platform-independent/Squeak%version-%origin-%major.zip
URL:           http://www.squeak.org
BuildRequires: unzip
Requires:      squeak-vm >= 3.0
Requires:      squeak-sources >= 3
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
These are the image and change files needed for the Squeak Virtual Machiene.

%build
mkdir -p %{buildroot}/extract/
unzip %{SOURCE0} -d %{buildroot}/extract/

%install
mkdir -p %{buildroot}%{_libdir}/squeak/
mv %{buildroot}/extract/Squeak%version-%origin-%major/Squeak*.changes %{buildroot}%{_libdir}/squeak/Squeak%version-%major.changes; gzip -9 %{buildroot}%{_libdir}/squeak/Squeak%version-%major.changes
cp %{buildroot}/extract/Squeak%version-%origin-%major/Squeak*.image %{buildroot}%{_libdir}/squeak/Squeak%version-%major.image; gzip -9 %{buildroot}%{_libdir}/squeak/Squeak%version-%major.image
rm -rf %{buildroot}/extract/

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{_libdir}/squeak/*

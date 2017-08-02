%{?scl:%scl_package isorelax}
%{!?scl:%global pkg_name %{name}}

# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%global cvstag  release-20050331

Name:           %{?scl_prefix}isorelax
Summary:        Public interfaces for RELAX Core
URL:            http://iso-relax.sourceforge.net/
Epoch:          1
Version:        0
# I can't use %%{cvstag} as dashes aren't allowed in Release tags
Release:        0.21.release20050331.1%{?dist}
License:        MIT and ASL 1.1
BuildArch:      noarch

# mkdir isorelax-release-20050331-src
# cd isorelax-release-20050331-src
# cvs -d:pserver:anonymous@iso-relax.cvs.sourceforge.net:/cvsroot/iso-relax \
#   export -r release-20050331 src lib
# cvs -d:pserver:anonymous@iso-relax.cvs.sourceforge.net:/cvsroot/iso-relax \
#   co -r release-20050331 build.xml
# rm -rf CVS
# cd ..
# tar cjf isorelax-release-20050331-src.tar.bz2 isorelax-release-20050331-src
Source0:        %{pkg_name}-%{cvstag}-src.tar.bz2
# There's no license in the upstream tarball so include it here
Source1:        license.txt
Source2:        http://repo2.maven.org/maven2/%{pkg_name}/%{pkg_name}/20030108/%{pkg_name}-20030108.pom
Patch0:         %{pkg_name}-apidocsandcompressedjar.patch

BuildRequires:  %{?scl_prefix}javapackages-local
BuildRequires:  %{?scl_prefix}ant

%description
The ISO RELAX project was started to host public interfaces 
useful for applications to support RELAX Core. Now, however,
some of the hosted material is schema language-neutral.

%package javadoc
Summary:        API documentation for %{pkg_name}

%description javadoc
%{summary}.

%prep
%setup -q -n %{pkg_name}-%{cvstag}-src
find -name "*.jar" -delete
ln -s %{_javadir}/ant.jar lib/
%patch0 -p0
cp %{SOURCE1} .

%build
ant release

%install
%mvn_file : %{pkg_name}
%mvn_artifact %{SOURCE2} %{pkg_name}.jar

%mvn_install -J apidocs

%files -f .mfiles
%license license.txt

%files javadoc -f .mfiles-javadoc
%license license.txt

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 1:0-0.21.release20050331.1
- Automated package import and SCL-ization

* Wed Mar 22 2017 Michael Simacek <msimacek@redhat.com> - 1:0-0.21.release20050331
- Install with XMvn

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0-0.20.release20050331
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0-0.19.release20050331
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0-0.18.release20050331
- Add build-requires on javapackages-local

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0-0.17.release20050331
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0-0.16.release20050331
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:0-0.15.release20050331
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0-0.14.release20050331
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0-0.13.release20050331
- Update to current packaging guidelines

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0-0.12.release20050331
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov  1 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0-0.11.release20050331
- Add maven POM

* Mon Oct 22 2012 Mat Booth <fedora@matbooth.co.uk> - 1:0-0.10.release20050331
- Include license text in %%doc section

* Sun Oct 21 2012 Mat Booth <fedora@matbooth.co.uk> - 1:0-0.9.release20050331
- A portion of /org/iso_relax/verifier/VerifierFactory.java is licenced under ASL 1.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0-0.8.release20050331
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 6 2012 Alexander Kurtakov <akurtako@redhat.com> 1:0-0.7.release20050331
- Update to current guidelines.
- Drop all fake BR/R now.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0-0.6.release20050331
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0-0.5.release20050331
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0-0.4.release20050331
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0-0.3.release20050331
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:0-0.2.release20050331
- drop repotag

* Thu May 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1:0-0.1.release20050331.1jpp.3
- fix license tag

* Tue Mar 06 2007 Vivek Lakshmanan <vivekl@redhat.com> 1:0-0.1.release20050331.1jpp.2.fc7
- Rebuild

* Tue Mar 06 2007 Vivek Lakshmanan <vivekl@redhat.com> 1:0-0.1.release20050331.1jpp.1.fc7
- First Fedora build

* Mon Feb 12 2007 Andrew Overholt <overholt@redhat.com> 1:0-0.1.release20050331.1jpp.1
- Clean up
- Remove tests
- Fix e:nvr for new scheme (0.Z.tag.Xjpp.Y%%{?dist}) and bump epoch for
  upgrades
- Add instructions for how to create source drop
- Don't do javadoc symlinking in %%post{,un}
- Remove Obsoletes and Provides on isorelax-bootstrap as they were never
  shipped in Fedora and I don't know what version to Obsolete/Provide

* Wed Mar 22 2006 Ralph Apel <r.apel at r-apel.de> 0:0.1-0.20041111.2jpp
- By default omit tests requiring xercesjarv
- Add postun for javadoc
- Drop useless macros for name, version, etc.

* Tue Aug 23 2005 Ralph Apel <r.apel at r-apel.de> 0:0.1-0.20041111.1jpp
- Upgrade to 20041111

* Fri Apr 22 2005 Fernando Nasser <fnasser@redhat.com> 0:0.1-0.20030108.3jpp
- Rebuild with standard version scheme

* Wed Aug 25 2004 Ralph Apel <r.apel at r-apel.de> 0:0.1-0.20030108.2jpp
- Build with ant-1.6.2

* Tue Jul 06 2004 Ralph Apel <r.apel at r-apel.de> 0:0.1-0.20030108.1jpp
- First build from sources into free section
- Use xercesjarv instead of swift as verifier impl

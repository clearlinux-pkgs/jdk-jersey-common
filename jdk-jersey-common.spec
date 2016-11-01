Name     : jdk-jersey-common
Version  : 2.22.2
Release  : 4
URL      : https://repo1.maven.org/maven2/org/glassfish/jersey/core/jersey-common/2.22.2/jersey-common-2.22.2.jar
Source0  : https://repo1.maven.org/maven2/org/glassfish/jersey/core/jersey-common/2.22.2/jersey-common-2.22.2.jar
Source1  : https://repo1.maven.org/maven2/org/glassfish/jersey/core/jersey-common/2.22.2/jersey-common-2.22.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : CDDL-1.0 GPL-1.0
Requires: jdk-jersey-common-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-jersey-common package.
Group: Data

%description data
data components for the jdk-jersey-common package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/jersey-common.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/jersey-common.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/jersey-common.xml \
%{buildroot}/usr/share/maven-poms/jersey-common.pom \
%{buildroot}/usr/share/java/jersey-common.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/jersey-common.jar
/usr/share/maven-metadata/jersey-common.xml
/usr/share/maven-poms/jersey-common.pom

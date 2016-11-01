PKG_NAME := jdk-jersey-common
URL := https://repo1.maven.org/maven2/org/glassfish/jersey/core/jersey-common/2.22.2/jersey-common-2.22.2.jar
ARCHIVES := https://repo1.maven.org/maven2/org/glassfish/jersey/core/jersey-common/2.22.2/jersey-common-2.22.2.pom %{buildroot}

include ../common/Makefile.common

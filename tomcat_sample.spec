Name:           replatform_tomcat8
Version:        3
Release:        0
###Release:     0%{?dist}
BuildArch:      noarch
Summary:        Apache Tomcat8

Group:          Apache
License:        GPL
URL:            NA
Source0:        apache-tomcat-8.5.55.tar.gz

# Do not try autogenerate prereq/conflicts/obsoletes and check files
AutoProv: no
AutoReq: no
%undefine __find_provides
%undefine __find_requires
%undefine __check_files
%undefine __find_prereq
%undefine __find_conflicts
%undefine __find_obsoletes
%undefine _missing_build_ids_terminate_build
%define __spec_install_post %{nil}
%define _binaries_in_noarch_packages_terminate_build 0
%define tomcatdir apache-tomcat-8.5.55

Requires:       /bin/sh
Provides:       apache-tomcat-8.5.55

%description
Apache Tomcat8 for ECOMM.

%prep
[ $RPM_BUILD_DIR != "/" ] && rm -rf $RPM_BUILD_DIR/%{tomcatdir}
cd $RPM_BUILD_DIR
zcat ${RPM_SOURCE_DIR}/%{tomcatdir}.tar.gz | tar -xvf -
###%setup -q

%pre
logger -p local0.notice "Installing Tomcat8 RPM Version 8.5.55..."

%preun
logger -p local0.notice "Uninstalling Tomcat8 RPM Version 8.5.55..."

%install
[ $RPM_BUILD_ROOT != "/" ] && rm -rf $RPM_BUILD_ROOT/
install -d -m 0755 ${RPM_BUILD_ROOT}/opt/fdbin/tomcat
cd $RPM_BUILD_DIR
cp --parents -dpr %{tomcatdir} ${RPM_BUILD_ROOT}/opt/fdbin/tomcat/
cd /root/rpmbuild
###make install DESTDIR=%{buildroot}/opt/fdbin/tomcat

%clean
[ $RPM_BUILD_DIR != "/" ] && rm -rf ${RPM_BUILD_DIR}/%{tomcatdir}
[ $RPM_BUILD_ROOT != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,fdadmin,fdadmin,-)
/opt/fdbin/tomcat/%{tomcatdir}

%doc

%post
cd /opt/fdbin/tomcat
unlink current
ln -s %{tomcatdir} current
ls -l /opt/fdbin/tomcat/current
cd current/webapps
echo "Deleting ROOT in webapps..."
rm -rf ROOT
cd manager/META-INF
echo "Inserting comments in managers context.xml..."
sed -i_ORG -e '/<Context .*privileged="true" >/a\
<!--' -e '/allow="127.* \/>/a\
-->' context.xml
cd

%changelog

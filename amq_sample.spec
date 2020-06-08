Name:           fd_apache-activemq
Version:        4
Release:        0
###Release:     0%{?dist}
BuildArch:      noarch
Summary:        Apache ActiveMQ Classic

Group:          Apache
License:        GPL
URL:            NA
###Source0:     apache-activemq-5.15.12-bin.tar.gz

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

Requires:       /bin/sh
Provides:       apache-activemq-5.15.12
Provides:       fd_apache-activemq-%{version}

%description
Apache ActiveMQ Classic for ECOMM.

%prep
###%setup -q

%pre
logger -p local0.notice "Installing ActiveMQ RPM..."

%preun
logger -p local0.notice "Uninstalling ActiveMQ RPM..."

%install
[ $RPM_BUILD_ROOT != "/" ] && rm -rf $RPM_BUILD_ROOT
install -d -m 0755 ${RPM_BUILD_ROOT}/opt/fdbin/activemq
cd /root
cp --parents -dpr activemq ${RPM_BUILD_ROOT}/opt/fdbin/
cd rpmbuild
###make install DESTDIR=%{buildroot}/opt/fdbin/activemq

%clean
[ $RPM_BUILD_ROOT != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,fdadmin,fdadmin,0755)
/opt/fdbin/activemq
%attr(0755, fdadmin, fdadmin) /opt/fdbin/activemq/apache-activemq-5.15.12/activemq-all-5.15.12.jar
%attr(0755, fdadmin, fdadmin) /opt/fdbin/activemq/apache-activemq-5.15.12/bin/activemq-diag
%attr(0755, fdadmin, fdadmin) /opt/fdbin/activemq/apache-activemq-5.15.12/bin/activemq
%attr(0755, fdadmin, fdadmin) /opt/fdbin/activemq/apache-activemq-5.15.12/bin/linux-x86-64/libwrapper.so
%attr(0755, fdadmin, fdadmin) /opt/fdbin/activemq/apache-activemq-5.15.12/bin/linux-x86-64/wrapper
%attr(0755, fdadmin, fdadmin) /opt/fdbin/activemq/apache-activemq-5.15.12/bin/linux-x86-64/activemq
%attr(0755, fdadmin, fdadmin) /opt/fdbin/activemq/apache-activemq-5.15.12/bin/linux-x86-32/libwrapper.so
%attr(0755, fdadmin, fdadmin) /opt/fdbin/activemq/apache-activemq-5.15.12/bin/linux-x86-32/wrapper
%attr(0755, fdadmin, fdadmin) /opt/fdbin/activemq/apache-activemq-5.15.12/bin/linux-x86-32/activemq
%attr(0755, fdadmin, fdadmin) /opt/fdbin/activemq/apache-activemq-5.15.12/bin/macosx/wrapper
%attr(0755, fdadmin, fdadmin) /opt/fdbin/activemq/apache-activemq-5.15.12/bin/macosx/activemq
%attr(0755, fdadmin, fdadmin) /opt/fdbin/activemq/apache-activemq-5.15.12/bin/macosx/libwrapper.jnilib
%attr(0755, fdadmin, fdadmin) /opt/fdbin/activemq/apache-activemq-5.15.12/examples/stomp/ruby/publisher.rb
%attr(0755, fdadmin, fdadmin) /opt/fdbin/activemq/apache-activemq-5.15.12/examples/stomp/ruby/listener.rb
%attr(0755, fdadmin, fdadmin) /opt/fdbin/activemq/apache-activemq-5.15.12/examples/stomp/ruby/catstomp.rb
%attr(0755, fdadmin, fdadmin) /opt/fdbin/activemq/apache-activemq-5.15.12/examples/stomp/ruby/stompcat.rb

%doc

%post
cd /opt/fdbin/activemq
unlink current
ln -s apache-activemq-5.15.12 current
ls -l /opt/fdbin/activemq/current
cd

%changelog

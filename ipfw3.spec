Summary: Dummynet driver and tool
Name: ipfw3
Version: 1.0
Release: 1
License: -
Group: Applications
Source: %{name}.tgz
URL: http://www.ericsson.com
Distribution: SUSE Linux
Vendor: Ericsson
Prefix: /

%description
ipfw kernel module and tool for dummynets

%prep
%autosetup -n %{name}

%build
make -f Makefile.suse KERNELPATH=/usr/src/linux all

%install
make -f Makefile.suse KERNELPATH=/usr/src/linux install

%clean
%{__rm} -rf %{buildroot}

%files
%attr(755, root, root) "%{prefix}/usr/sbin/ipfw"
%attr(755, root, root) "%{prefix}/lib/modules/%(uname -r)/kernel/net/ipv4/ipfw_mod.ko"

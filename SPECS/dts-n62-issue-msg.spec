BuildArch:      noarch
Name:           dts-n62-issue-msg
Version:        1.2.0
Release:        1
License:        GPLv3
Group:          Unspecified
Summary:        A systemd service that regenerates the DTS N62 issue message every 5 minutes
Distribution:   PhotonPonyOS

URL:            https://github.com/AP-Sensing/dts-n62-issue-msg/tree/ppos38
Vendor:         AP Sensing
Packager:       AP Sensing
Provides:       dts-n62-issue-msg = %{version}-%{release}

%{?systemd_requires}

Source0:        %{_sourcedir}/dts-n62-issue-msg
Source1:        %{_sourcedir}/dts-n62-issue-msg-gen
Source2:        %{_sourcedir}/dts-n62-issue-msg.service
Source3:        %{_sourcedir}/dts-n62-issue-msg.timer
Source4:        %{_sourcedir}/42-dts-n62-issue-msg.preset

%description
A systemd service that regenerates the DTS N62 issue message every 5 minutes.

%prep

%build

%pre

%post
%systemd_post dts-n62-issue-msg.service dts-n62-issue-msg.timer

%postun
%systemd_postun_with_restart dts-n62-issue-msg.service dts-n62-issue-msg.timer

%preun
%systemd_preun dts-n62-issue-msg.service dts-n62-issue-msg.timer

%install
install -d -m 755 $RPM_BUILD_ROOT/usr/bin/
install -m 755 %{_sourcedir}/dts-n62-issue-msg $RPM_BUILD_ROOT/usr/bin
install -m 755 %{_sourcedir}/dts-n62-issue-msg-gen $RPM_BUILD_ROOT/usr/bin

install -d -m 755 $RPM_BUILD_ROOT/usr/lib/systemd/system
install -m 644 %{_sourcedir}/dts-n62-issue-msg.service $RPM_BUILD_ROOT/usr/lib/systemd/system
install -m 644 %{_sourcedir}/dts-n62-issue-msg.timer $RPM_BUILD_ROOT/usr/lib/systemd/system

install -d -m 755 $RPM_BUILD_ROOT/usr/lib/systemd/system-preset
install -m 644 %{_sourcedir}/42-dts-n62-issue-msg.preset $RPM_BUILD_ROOT/usr/lib/systemd/system-preset

%files
%attr(755, root, root) /usr/bin/dts-n62-issue-msg
%attr(755, root, root) /usr/bin/dts-n62-issue-msg-gen

%attr(644, root, root) /usr/lib/systemd/system/dts-n62-issue-msg.service
%attr(644, root, root) /usr/lib/systemd/system/dts-n62-issue-msg.timer

%attr(644, root, root) /usr/lib/systemd/system-preset/42-dts-n62-issue-msg.preset

%ghost /etc/issue.d/dts-n62.issue

%changelog
* Wed Oct 11 2023 Fabian Sauter <fabian.sauter+rpm@apsensing.com> - 1.2.0-1
- Make sure we run the service before the tty appears

* Mon Oct 09 2023 Fabian Sauter <fabian.sauter+rpm@apsensing.com> - 1.1.0-1
- Run the service after the network is online

* Thu Oct 05 2023 Fabian Sauter <fabian.sauter+rpm@apsensing.com> - 1.0.0-1
- Initial release

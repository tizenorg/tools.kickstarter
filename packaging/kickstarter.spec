%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
Name:       kickstarter
Summary:    Create kickstart files for meego images
Version:    0.15
Release:    %{?release_prefix:%{release_prefix}.}1.33.%{?dist}%{!?dist:tizen}
VCS:        magnolia/tools/kickstarter#submit/trunk/20121214.020151-0-gb84005640685a909e910b63595e25208822ab7fd
Group:      System/Base
License:    GPLv2
BuildArch:  noarch
URL:        http://www.meego.com
Source0:    %{name}-%{version}.tar.bz2
Requires:   python-yaml
#Requires:   python-urlgrabber
Requires:   python-cheetah
Requires:   python-lxml
BuildRequires:  python-devel
BuildRequires:  python-cheetah


%description
Create Configuration files to build meego images



%prep
%setup -q -n %{name}-%{version}


%build
make tmpls

CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%if 0%{?suse_version}
%{__python} setup.py install --root=$RPM_BUILD_ROOT --prefix=%{_prefix}
%else
%{__python} setup.py install --root=$RPM_BUILD_ROOT -O1 --prefix=%{_prefix}
%endif







%files
%defattr(-,root,root,-)
%{_bindir}/*
%{python_sitelib}/*


%changelog
* Mon Sep 16 2013 .jang@samsung.com> - submit/trunk/20121214.020151 
- PROJECT: magnolia/tools/kickstarter
- COMMIT_ID: b84005640685a909e910b63595e25208822ab7fd
- PATCHSET_REVISION: b84005640685a909e910b63595e25208822ab7fd
- CHANGE_OWNER: \"Yeongil Jang\" <yg0577.jang@samsung.com>
- PATCHSET_UPLOADER: \"Yeongil Jang\" <yg0577.jang@samsung.com>
- CHANGE_URL: http://slp-info.sec.samsung.net/gerrit/125832
- PATCHSET_REVISION: b84005640685a909e910b63595e25208822ab7fd
- TAGGER: Yeongil Jang <yg0577.jang@samsung.com>
- Gerrit patchset approval info:
- Newton Lee <newton.lee@samsung.com> Code Review : 2
- Yeongil Jang <yg0577.jang@samsung.com> Verified : 1
- CHANGE_SUBJECT: add '%%attachment' section for mic container
- [Project] GT-I8800
- [Title] Add '%%attachment' section for mic container
- [BinType] PDA
- [Customer] Open
- [Issue#] N/A
- [Problem] N/A
- [Cause] N/A
- [Solution] Add '%%attachment' section for mic container
- [Team] SCM
- [Developer] Yeongil Jang <yg0577.jang@samsung.com>
- [Request] N/A
- [Horizontal expansion] N/A
- [SCMRequest] N/A
* Fri May 18 2012 Jian-feng Ding <jian-feng.ding@intel.com> - 0.15
- update to latest
* Mon Jul  4 2011 Li Yi <yix.li@intel.com> - 0.12
- make Active keyword works
* Fri May 27 2011 Anas Nashif <anas.nashif@intel.com> - 0.11
- enhance bootloader option support
* Wed May 18 2011 Anas Nashif <anas.nashif@intel.com> - 0.10
- Support bootloader options (bmc #16408)
* Fri May  6 2011 Anas Nashif <anas.nashif@intel.com> - 0.9
- Now require python-yaml
* Mon May  2 2011 Anas Nashif <anas.nashif@intel.com> - 0.9
- Fixed bmc #16397 -  temporary .yaml~ files are read
* Sat Apr  2 2011 Anas Nashif <anas.nashif@intel.com> - 0.8
- Support external configurations
- Support additional keywords to keep up with static ks files
- 0.8
* Fri Mar 18 2011 Anas Nashif <anas.nashif@intel.com> - 0.7
- Fix schedule handling.
* Thu Mar 17 2011 Anas Nashif <anas.nashif@intel.com> - 0.6
- Use cron style syntax for schedule
- Fixed path where files are stored on repo
* Wed Mar 16 2011 Anas Nashif <anas.nashif@intel.com> - 0.5
- Add python-lxml as a runtime dependency
* Wed Mar 16 2011 Anas Nashif <anas.nashif@intel.com> - 0.5
- Create index file with all kickstart files
* Sun Feb  6 2011 Anas Nashif <anas.nashif@intel.com> - 0.4
- Make it build on other distros
* Wed Jan 26 2011 Anas Nashif <anas.nashif@intel.com> - 0.2
- Initial Release

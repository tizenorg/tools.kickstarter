#!/usr/bin/env python

import os, sys
from distutils.core import setup
try:
    import setuptools
    # enable "setup.py develop", optional
except ImportError:
    pass

MOD_NAME = 'kickstart'

version_path = 'VERSION'
if not os.path.isfile(version_path):
    print 'No VERSION file in topdir, abort'
    sys.exit(1)

try:
    # first line should be the version number
    version = open(version_path).readline().strip()
    if not version:
        print 'VERSION file is invalid, abort'
        sys.exit(1)

    ver_file = open('%s/__version__.py' % MOD_NAME, 'w')
    ver_file.write("VERSION = \"%s\"\n" % version)
    ver_file.close()
except IOError:
    print 'WARNING: Cannot write version number file'

setup(name='kickstarter',
      version = version,
      description='Kickstarter',
      author='Anas Nashif',
      author_email='anas.nashif@intel.com',
      url='http://meego.com/',
      scripts=['tools/kickstarter'],
      packages=['kickstart', 'kswriter']
     )


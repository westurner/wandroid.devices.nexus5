#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='wandroid.devices.nexus5',
    version='0.1.0',
    description='Nexus 5 Utilities',
    long_description=readme + '\n\n' + history,
    author='Wes Turner',
    author_email='wes@wrd.nu',
    url='https://bitbucket.org/westurner/wandroid.devices.nexus5',
    packages = find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    namespace_packages = [
        'wandroid',
        'wandroid.devices',
    ],
    entry_points = {
        'wandroid_devices': [
            'nexus5 = wandroid.devices.nexus5:Nexus5'
        ]
    },
    package_dir={'wandroid.devices.nexus5': 'wandroid'},
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='android wandroid nexus5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)

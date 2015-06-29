#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The setup script for the Mt. Olympus library.

.. moduleauthor:: hbldh <henrik.blidh@swedwise.com>

Created on 2014-02-14, 16:20

"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from setuptools import setup, find_packages

setup(
    name='restpyberryimu',
    version="0.1.0",
    description='',
    author='Henrik Blidh',
    author_email='henrik.blidh@nedomkull.com',
    license='MIT',
    url='https://www.github.com/hbldh/pyberryimu-rest',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pyberryimu>=0.3.0',
        'Flask>=0.10.1',
        'Flask-WTF>=0.10.1',
    ],
    dependency_links=[
        'git+https://github.com/hbldh/pyberryimu.git@v.0.3.0#egg=pyberryimu-0.3.0',
    ],
    ext_modules=[],
)

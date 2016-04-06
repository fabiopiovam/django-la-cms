#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os.path import join, dirname
import sys

from pip.req import parse_requirements
from setuptools import setup, find_packages

# allow setup.py to be run from any path and open files
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

ROOT = dirname(__file__)

try:
    README = open('README.md').read()
except:
    README = None

def get_requirements(filename):
    install_requires = []
    dependency_links = []
    
    dependency_links = [line.strip()
            for line in open(join(ROOT, filename))
            if '://' in line]
    
    for r in parse_requirements(filename, session=False):
        install_requires.append(str(r.req))
        
    return install_requires, dependency_links

install_requires, dependency_links = get_requirements('requirements.txt')
print install_requires
print dependency_links
setup(
    name='django-la-cms',
    version="v0.1.0",
    description=(
        'Django app for a simple content management system'
    ),
    long_description=README,
    install_requires=install_requires,
    dependency_links=dependency_links,
    author='Fábio Piovam Elias',
    author_email='fabio@laborautonomo.org',
    url='https://github.com/laborautonomo/django-la-cms/',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)

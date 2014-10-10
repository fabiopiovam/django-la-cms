#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

try:
    README = open('README.md', encoding='utf-8').read()
except:
    README = None

try:
    REQUIREMENTS = open('requirements.txt', encoding='utf-8').read()
except:
    REQUIREMENTS = None

setup(
    name='django-la-cms',
    version="v0.1.0",
    description=(
        'Django app for a simple content management system'
    ),
    long_description=README,
    install_requires=REQUIREMENTS,
    dependency_links = [
        'https://github.com/laborautonomo/django-la-tags/archive/v0.1.0.tar.gz#egg=django-la-tags',
    ],
    author='Fábio Piovam Elias',
    author_email='fabio@laborautonomo.org',
    url='https://github.com/laborautonomo/django-la-cms/',
    packages=find_packages(),
    include_package_data=True,
)
#!/usr/bin/env python

from setuptools import setup, find_packages

try:
    README = open('README.md').read()
except:
    README = None

try:
    REQUIREMENTS = open('requirements.txt').read()
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
        '-e git://github.com/laborautonomo/django-la-tags.git@4ea8e416933bb56e49f43dffcb8e2990c0e860a6#egg=django-la-tags',
    ],
    author='Fábio Piovam Elias',
    author_email='fabio@laborautonomo.org',
    url='https://github.com/laborautonomo/django-la-cms/',
    packages=find_packages(),
    include_package_data=True,
)
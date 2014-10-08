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
    install_requires=[
        'Django>=1.4.10',
        'django-admin-sortable==1.7.3',
        'django-ckeditor-updated==4.4.0',
        '-e git://github.com/laborautonomo/django-la-tags.git#egg=django-la-tags',
    ],
    author='Fábio Piovam Elias',
    author_email='fabio@laborautonomo.org',
    url='https://github.com/laborautonomo/django-la-cms/',
    packages=find_packages(),
    include_package_data=True,
)
# django-la-cms

Django app for a simple content management system

## Install

- Execute:
    pip install -e git+git://github.com/laborautonomo/django-la-cms.git#egg=django-la-cms

- Install django-la-tags required:
    pip install -e git+git://github.com/laborautonomo/django-la-tags.git#egg=django-la-tags

## Usage

- Config app in `settings.py`:
        INSTALLED_APPS = [
            ...

            'tags.apps.TagsConfig',
            'cms.apps.CmsConfig',

            ...
        ]

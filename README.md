# django-la-cms

Django app for a simple content management system

## Install

- Execute:
    pip install -e git+git://github.com/laborautonomo/django-la-cms.git@v0.3.0#egg=django-la-cms

- Install django-la-tags required:
    pip install -e git+git://github.com/laborautonomo/django-la-tags.git@v0.4.0#egg=django-la-tags

## Usage

- Config app in `settings.py`:
        INSTALLED_APPS = [
            ...

            'tags.apps.TagsConfig',
            'cms.apps.CmsConfig',

            ...
        ]

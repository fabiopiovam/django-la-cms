# -*- coding: utf-8 -*-

"""
DocString for views.py.

Created by Fábio Piovam Elias - fabio@laborautonomo.org
laborautonomo.org (C) 2013

Notes: view to django-la-cms
"""


from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist

from .models import Page


def pages(request, category_slug=''):
    try:
        if not category_slug:
            pages = Page.activated.all()
        else:
            pages = Page.activated.filter(category__slug=category_slug)

    except ObjectDoesNotExist:
        pages = None

    return render_to_response('cms/list_pages.html',
                              {'pages': pages})


def page(request, slug):
    try:
        page = Page.activated.get(slug=slug)
    except ObjectDoesNotExist:
        page = None

    return render_to_response('cms/page.html',
                              {'page': page, })

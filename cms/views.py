# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.exceptions import ObjectDoesNotExist

from models import Page


def pages(request, category_slug=''):
    try:
        if not category_slug:
            pages = Page.activated.all()
        else:
            pages = Page.activated.filter(category__slug=category_slug)
        
    except ObjectDoesNotExist:
        pages = None
    
    template = loader.get_template('cms/list_pages.html')
    context = RequestContext(request, {
        'pages'  : pages,
    })
    return HttpResponse(template.render(context))

def page(request,slug):
    
    try:
        page = Page.activated.get(slug=slug)
    except ObjectDoesNotExist:
        page = None
    
    template = loader.get_template('cms/page.html')
    context = RequestContext(request, {
        'page'  : page,
    })
    return HttpResponse(template.render(context))
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django import forms
from adminsortable.admin import SortableAdmin

from cms.models import Category, Page
from tags.forms import set_tags, FormTags


class FormPage(FormTags):

    class Meta:
        model = Page
        fields = '__all__'


class PageAdmin(SortableAdmin):
    list_display = ('title', 'published')
    search_fields = ['title', 'slug']
    list_filter = ['category__title', 'published']
    fields = ('title', 'content', 'category', 'tags', 'published')
    filter_horizontal = ('category',)

    form = FormPage

    def save_model(self, request, obj, form, change):
        super(PageAdmin, self).save_model(request, obj, form, change)

        set_tags(obj, form.cleaned_data['tags'])


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ['title', 'slug']
    fields = ('title',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)

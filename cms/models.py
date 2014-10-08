# -*- coding: utf-8 -*-

from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField
from adminsortable.models import Sortable

class Category(models.Model):
    def __unicode__(self):
        return u'%s' % self.title
    
    class Meta:
        verbose_name = u"categoria"
    
    def save(self, *args, **kwargs):
        if not self.id:
            super(Category, self).save(*args, **kwargs)
            self.slug = slugify(self.title.strip())
        super(Category, self).save(*args, **kwargs)
    
    title = models.CharField(u'Categoria', max_length=80)
    slug = models.SlugField(max_length=100, unique=True)

class PageActivatedManager(models.Manager):
    def get_queryset(self):
        return super(PageActivatedManager, self).get_queryset().filter(published=True).order_by('order')

class Page(Sortable):
    def __unicode__(self):
        return u'%s' % self.title
    
    def get_absolute_url(self):
        return reverse('page', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = u"página"
    
    def save(self, *args, **kwargs):
        if not self.id:
            super(Page, self).save(*args, **kwargs)
            self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)
    
    category = models.ManyToManyField(Category, verbose_name=u"Categoria", null=True, blank=True)
    title = models.CharField(u'Título', max_length=100)
    slug = models.SlugField(max_length=120)
    content =  RichTextField(verbose_name=u'Conteúdo')
    
    published = models.BooleanField(u'Publicado', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    u''' Managers '''
    objects     = models.Manager()
    activated   = PageActivatedManager()
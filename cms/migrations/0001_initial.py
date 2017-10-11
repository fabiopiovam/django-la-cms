# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 16:53
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Categoria')),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'categoria',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('title', models.CharField(max_length=100, verbose_name='T\xedtulo')),
                ('slug', models.SlugField(max_length=120)),
                ('content', ckeditor.fields.RichTextField(verbose_name='Conte\xfado')),
                ('published', models.BooleanField(default=True, verbose_name='Publicado')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(blank=True, to='cms.Category', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'p\xe1gina',
            },
        ),
    ]

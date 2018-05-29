# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-05-18 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.URLField(blank=True, null=True)),
                ('name', models.CharField(max_length=160)),
                ('slug_name', models.SlugField(max_length=350)),
                ('description', models.TextField()),
                ('url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url_list', models.ManyToManyField(to='links.Links')),
            ],
            options={
                'db_table': 'movies',
            },
        ),
    ]

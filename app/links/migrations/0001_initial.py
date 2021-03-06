# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-05-18 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.URLField(blank=True, null=True)),
                ('name', models.CharField(max_length=160)),
                ('slug_name', models.SlugField(max_length=350)),
                ('description', models.TextField(null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'links',
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-05-18 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='url_list',
            field=models.ManyToManyField(blank=True, to='links.Links'),
        ),
    ]

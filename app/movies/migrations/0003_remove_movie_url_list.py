# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-05-29 10:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20180518_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='url_list',
        ),
    ]
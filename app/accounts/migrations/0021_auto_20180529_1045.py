# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-05-29 10:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20180518_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 29, 10, 45, 31, 442014)),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-05-18 17:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20180518_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 18, 17, 46, 42, 990010)),
        ),
    ]

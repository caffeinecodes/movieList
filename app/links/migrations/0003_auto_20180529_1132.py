# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-05-29 11:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_auto_20180529_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='series.MovieSeries'),
        ),
    ]
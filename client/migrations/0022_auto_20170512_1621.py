# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-12 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0021_auto_20170512_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
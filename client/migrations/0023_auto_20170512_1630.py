# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-12 16:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0022_auto_20170512_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
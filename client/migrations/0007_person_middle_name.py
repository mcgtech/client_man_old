# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-12 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_auto_20170512_0707'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='middle_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]

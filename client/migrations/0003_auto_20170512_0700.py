# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-12 07:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20170512_0651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='known_as',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='person',
            name='title',
        ),
    ]

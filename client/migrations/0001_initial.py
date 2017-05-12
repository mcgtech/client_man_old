# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-11 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.IntegerField(choices=[(0, 'Mr'), (1, 'Mrs'), (2, 'Miss'), (3, 'Ms')], default=0)),
                ('sex', models.IntegerField(choices=[(0, 'Male'), (1, 'Female')], default=0)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('known_as', models.CharField(max_length=100)),
                ('dob', models.DateField()),
            ],
        ),
    ]

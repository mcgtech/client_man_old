# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-12 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0014_auto_20170512_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='birth_certificate',
            field=models.FileField(null=True, upload_to='client/birth_certs/'),
        ),
    ]

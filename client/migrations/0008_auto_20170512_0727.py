# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-12 07:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0007_person_middle_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(default='', max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='notes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.Note'),
        ),
    ]

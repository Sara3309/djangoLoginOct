# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-19 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=None, max_length=255),
        ),
    ]

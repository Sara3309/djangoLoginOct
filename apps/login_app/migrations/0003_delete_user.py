# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-19 02:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_user_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]

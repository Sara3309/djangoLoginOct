# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-19 21:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0004_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_received', to='login_app.User')),
                ('comment_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_sent', to='login_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_receiver', to='login_app.User')),
                ('message_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_sender', to='login_app.User')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_belonged', to='login_app.Message'),
        ),
    ]

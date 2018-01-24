# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch_controller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookmarkTb',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('post_id', models.BigIntegerField(blank=True, null=True)),
                ('user_id', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bookmark_tb',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CommentTb',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('is_display', models.TextField(blank=True, null=True)),
                ('text', models.CharField(blank=True, max_length=255, null=True)),
                ('user_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'comment_tb',
                'managed': False,
            },
        ),
    ]

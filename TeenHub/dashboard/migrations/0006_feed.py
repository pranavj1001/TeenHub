# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-07 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0005_delete_feed'),
    ]

    operations = [
        migrations.CreateModel(
            name='feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdBy', models.IntegerField()),
                ('message', models.CharField(max_length=200)),
                ('createdAt', models.IntegerField()),
                ('comments', models.IntegerField(default=0)),
            ],
        ),
    ]
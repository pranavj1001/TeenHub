# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-15 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('movie_id', models.IntegerField()),
                ('ratings', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
    ]

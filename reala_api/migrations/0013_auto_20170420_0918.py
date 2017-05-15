# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reala_api', '0012_auto_20170412_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='called',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='claimed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='mailed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='other',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='social',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reala_api', '0006_auto_20170406_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='email_address',
            field=models.CharField(default=None, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='gender',
            field=models.CharField(default=None, max_length=16, null=True),
        ),
    ]

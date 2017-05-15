# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reala_api', '0010_auto_20170411_1307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-occurred']},
        ),
        migrations.AlterField(
            model_name='event',
            name='occurred',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='parcel',
            name='city',
            field=models.CharField(default=None, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='parcel',
            name='postal_code',
            field=models.CharField(default=None, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='parcel',
            name='route',
            field=models.CharField(default=None, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='parcel',
            name='state',
            field=models.CharField(default=None, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='parcel',
            name='street_number',
            field=models.CharField(default=None, max_length=16, null=True),
        ),
    ]
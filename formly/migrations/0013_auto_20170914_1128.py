# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-14 16:28
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formly', '0012_auto_20170912_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='mapping',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}),
        ),
    ]

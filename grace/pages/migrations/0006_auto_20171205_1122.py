# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-05 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_settings'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='page',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 07:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sermons', '0003_auto_20171018_1015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sermon',
            old_name='date_of_sermon',
            new_name='date',
        ),
    ]
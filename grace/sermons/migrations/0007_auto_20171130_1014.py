# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-30 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sermons', '0006_auto_20171114_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biblebook',
            name='part_of_bible',
            field=models.CharField(choices=[('ot', 'Ветхий Завет'), ('nt', 'Новый Завет')], default='nt', max_length=2),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-19 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20180220_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('future_events', 'Предстоящее событие'), ('news', 'Новость')], default='news', max_length=20),
        ),
    ]
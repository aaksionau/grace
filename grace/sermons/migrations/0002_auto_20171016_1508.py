# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sermons', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='biblebook',
            options={'verbose_name': 'книга Библии', 'verbose_name_plural': 'книги Библии'},
        ),
        migrations.AlterModelOptions(
            name='preacher',
            options={'verbose_name': 'проповедник', 'verbose_name_plural': 'проповедники'},
        ),
        migrations.AlterModelOptions(
            name='sermon',
            options={'verbose_name': 'проповедь', 'verbose_name_plural': 'проповеди'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'тема проповеди', 'verbose_name_plural': 'темы проповедей'},
        ),
        migrations.AlterField(
            model_name='sermon',
            name='date_of_sermon',
            field=models.DateField(),
        ),
    ]

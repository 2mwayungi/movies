# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-04-28 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_album_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist1',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='genre1',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
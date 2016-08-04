# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-04 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlexpander', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url_address',
            name='created_date',
        ),
        migrations.AlterField(
            model_name='url_address',
            name='full_url',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='url_address',
            name='http_status',
            field=models.IntegerField(),
        ),
    ]

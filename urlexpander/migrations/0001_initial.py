# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-02 20:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url_Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_url', models.CharField(max_length=50)),
                ('full_url', models.CharField(max_length=250)),
                ('http_status', models.TextField()),
                ('page_title', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
            ],
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-27 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_auto_20170224_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='time_attached',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

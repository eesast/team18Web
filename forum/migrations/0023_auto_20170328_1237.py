# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-28 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0022_auto_20170328_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfile',
            name='permissions',
            field=models.CharField(choices=[('2', '登陆可见'), ('1', '公开')], max_length=1),
        ),
    ]
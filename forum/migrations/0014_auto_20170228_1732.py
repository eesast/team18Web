# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0013_merge_20170228_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfile',
            name='permissions',
            field=models.CharField(choices=[('1', '公开'), ('2', '登陆可见')], max_length=1),
        ),
    ]

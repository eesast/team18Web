# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-18 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20170228_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='login_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
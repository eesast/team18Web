# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-24 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fight', '0002_auto_20170225_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='result',
            field=models.CharField(choices=[('2', 'tie'), ('1', 'AI2_wins'), ('0', 'AI1_wins')], max_length=1),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-01 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fight', '0011_player_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='ai',
            field=models.FileField(blank=True, null=True, upload_to='../../../ts18/submits'),
        ),
    ]

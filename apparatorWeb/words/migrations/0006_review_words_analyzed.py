# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-01 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0005_auto_20180331_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='words_analyzed',
            field=models.BooleanField(default=False),
        ),
    ]

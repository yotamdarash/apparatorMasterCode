# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-02 20:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0007_auto_20180402_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewword',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='words.Review'),
        ),
    ]

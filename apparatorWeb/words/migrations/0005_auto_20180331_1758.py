# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-31 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0004_auto_20180330_0647'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='modified_month',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='modified_week',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='modified_year',
            field=models.IntegerField(null=True),
        ),
    ]
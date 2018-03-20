# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-20 05:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('store_front', models.CharField(max_length=2)),
                ('app_version', models.CharField(max_length=32)),
                ('last_modified', models.DateTimeField(verbose_name='date published')),
                ('nickname', models.CharField(max_length=128)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('title', models.CharField(max_length=255)),
                ('review', models.TextField()),
                ('edited', models.NullBooleanField()),
            ],
        ),
    ]
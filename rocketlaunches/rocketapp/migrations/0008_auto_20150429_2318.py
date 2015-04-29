# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rocketapp', '0007_auto_20150429_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launch',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 4, 29, 23, 18, 42, 338941)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='payload',
            name='description',
            field=models.CharField(blank=True, null=True, max_length=2000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='payload',
            name='url',
            field=models.CharField(blank=True, null=True, max_length=2000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='payload',
            name='wiki_url',
            field=models.CharField(blank=True, null=True, max_length=2000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 4, 29, 23, 18, 42, 336108)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 4, 29, 23, 18, 42, 340510)),
            preserve_default=True,
        ),
    ]

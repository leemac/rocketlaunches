# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rocketapp', '0002_auto_20150429_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launch',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 4, 29, 12, 22, 32, 281288)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='country',
            field=models.CharField(max_length=10, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='description',
            field=models.CharField(max_length=2000, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='wiki_url',
            field=models.CharField(max_length=2000, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 4, 29, 12, 22, 32, 279986)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 4, 29, 12, 22, 32, 283353)),
            preserve_default=True,
        ),
    ]

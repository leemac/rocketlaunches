# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rocketapp', '0004_auto_20150429_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launch',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 12, 25, 12, 164524), verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 12, 25, 12, 163121), verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='description',
            field=models.CharField(null=True, blank=True, max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 12, 25, 12, 166918), verbose_name='date created'),
            preserve_default=True,
        ),
    ]

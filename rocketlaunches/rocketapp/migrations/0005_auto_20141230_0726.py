# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rocketapp', '0004_auto_20141229_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='launch',
            name='launch_url',
            field=models.CharField(null=True, max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='launch',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 30, 7, 26, 2, 806849), verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 30, 7, 26, 2, 805848), verbose_name='date created'),
            preserve_default=True,
        ),
    ]

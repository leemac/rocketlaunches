# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rocketapp', '0006_auto_20141231_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='rocket',
            name='manufacturer',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='launch',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2014, 12, 31, 16, 12, 13, 548902)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2014, 12, 31, 16, 12, 13, 547899)),
            preserve_default=True,
        ),
    ]

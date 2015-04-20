# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rocketapp', '0015_auto_20150415_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launch',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 4, 16, 0, 15, 38, 174416)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 4, 16, 0, 15, 38, 173518)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 4, 16, 0, 15, 38, 174962)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.CharField(max_length=200, default=''),
            preserve_default=True,
        ),
    ]

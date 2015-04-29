# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rocketapp', '0008_auto_20150429_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launch',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 4, 29, 23, 19, 52, 74265)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='url',
            field=models.CharField(max_length=2000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 4, 29, 23, 19, 52, 71448)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 4, 29, 23, 19, 52, 75980)),
            preserve_default=True,
        ),
    ]

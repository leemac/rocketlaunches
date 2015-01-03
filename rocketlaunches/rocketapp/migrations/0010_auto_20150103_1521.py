# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rocketapp', '0009_auto_20150103_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='launch',
            name='payload_purpose',
            field=models.CharField(max_length=2000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='launch',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 1, 3, 15, 21, 12, 684027)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 1, 3, 15, 21, 12, 684027)),
            preserve_default=True,
        ),
    ]

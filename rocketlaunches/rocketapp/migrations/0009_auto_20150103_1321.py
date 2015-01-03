# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rocketapp', '0008_auto_20150102_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='rocket',
            name='payload_to_gso',
            field=models.DecimalField(max_digits=8, null=True, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='launch',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 3, 13, 21, 54, 549467), verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 3, 13, 21, 54, 549467), verbose_name='date created'),
            preserve_default=True,
        ),
    ]

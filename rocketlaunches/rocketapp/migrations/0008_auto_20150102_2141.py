# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rocketapp', '0007_auto_20141231_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launch',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 2, 21, 41, 34, 936011), verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='cost',
            field=models.DecimalField(max_digits=15, null=True, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='cost_year',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 2, 21, 41, 34, 934995), verbose_name='date created'),
            preserve_default=True,
        ),
    ]

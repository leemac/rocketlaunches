# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rocketapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launch',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 12, 14, 7, 672741), verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 12, 14, 7, 671405), verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 12, 14, 7, 674805), verbose_name='date created'),
            preserve_default=True,
        ),
    ]

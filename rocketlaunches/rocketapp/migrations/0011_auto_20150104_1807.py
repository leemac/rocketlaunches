# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rocketapp', '0010_auto_20150103_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launch',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 4, 18, 7, 32, 398310), verbose_name=b'date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 4, 18, 7, 32, 397077), verbose_name=b'date created'),
            preserve_default=True,
        ),
    ]

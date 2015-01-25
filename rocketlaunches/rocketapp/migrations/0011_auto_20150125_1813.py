# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rocketapp', '0010_auto_20150103_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='launch',
            name='launch_date_tbd',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='launch',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 1, 25, 18, 13, 43, 202457)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 1, 25, 18, 13, 43, 201456)),
            preserve_default=True,
        ),
    ]

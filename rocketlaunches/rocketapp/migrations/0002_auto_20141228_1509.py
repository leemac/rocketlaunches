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
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 28, 15, 9, 5, 390970), verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='launch',
            name='launch_date',
            field=models.DateTimeField(null=True, blank=True, verbose_name='date launched'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='launch',
            name='updated_date',
            field=models.DateTimeField(null=True, blank=True, verbose_name='date updated'),
            preserve_default=True,
        ),
    ]

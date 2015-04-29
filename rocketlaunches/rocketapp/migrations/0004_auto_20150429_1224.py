# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rocketapp', '0003_auto_20150429_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launch',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 12, 24, 42, 289276), verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='cost',
            field=models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=15),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='cost_year',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 12, 24, 42, 287965), verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='payload_to_gso',
            field=models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=8),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='payload_to_gto',
            field=models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=8),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='payload_to_leo',
            field=models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=8),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='payload_to_sso',
            field=models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=8),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 12, 24, 42, 291376), verbose_name='date created'),
            preserve_default=True,
        ),
    ]

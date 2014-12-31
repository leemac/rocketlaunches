# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rocketapp', '0003_auto_20141229_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launch',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2014, 12, 29, 7, 12, 43, 286119)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2014, 12, 29, 7, 12, 43, 285115)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='payload_to_gto',
            field=models.DecimalField(null=True, decimal_places=2, max_digits=8),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='payload_to_leo',
            field=models.DecimalField(null=True, decimal_places=2, max_digits=8),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='payload_to_sso',
            field=models.DecimalField(null=True, decimal_places=2, max_digits=8),
            preserve_default=True,
        ),
    ]

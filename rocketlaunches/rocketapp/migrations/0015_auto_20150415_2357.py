# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rocketapp', '0014_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 4, 15, 23, 57, 40, 439467))),
                ('updated_date', models.DateTimeField(blank=True, verbose_name='date updated', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='launch',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 4, 15, 23, 57, 40, 438909)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 4, 15, 23, 57, 40, 438001)),
            preserve_default=True,
        ),
    ]

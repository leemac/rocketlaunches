# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rocketapp', '0006_auto_20150429_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayloadFamily',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='payload',
            name='payload_family',
            field=models.ForeignKey(default='', to='rocketapp.PayloadFamily', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='launch',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 12, 28, 52, 709255), verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 12, 28, 52, 706469), verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 12, 28, 52, 710867), verbose_name='date created'),
            preserve_default=True,
        ),
    ]

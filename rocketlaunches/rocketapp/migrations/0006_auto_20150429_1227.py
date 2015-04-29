# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rocketapp', '0005_auto_20150429_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='RocketFamily',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, null=True, max_length=2000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='launch',
            name='payloads',
            field=models.ManyToManyField(default='', to='rocketapp.Payload'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rocket',
            name='rocket_family',
            field=models.ForeignKey(blank=True, default='', to='rocketapp.RocketFamily', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='launch',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 12, 27, 46, 220106), verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rocket',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 12, 27, 46, 217664), verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 12, 27, 46, 221608), verbose_name='date created'),
            preserve_default=True,
        ),
    ]

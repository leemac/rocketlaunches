# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Launch',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('launch_date', models.DateTimeField(verbose_name='date launched', blank=True)),
                ('created_date', models.DateTimeField(verbose_name='date created', default=datetime.datetime(2014, 12, 28, 15, 7, 19, 288525))),
                ('updated_date', models.DateTimeField(verbose_name='date updated', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

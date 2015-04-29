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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('country', models.CharField(max_length=10, default='')),
                ('remarks', models.CharField(max_length=2000, null=True, blank=True)),
                ('customer', models.CharField(max_length=2000, null=True, blank=True)),
                ('customer_url', models.CharField(max_length=2000, null=True, blank=True)),
                ('payload', models.CharField(max_length=2000, null=True, blank=True)),
                ('payload_purpose', models.CharField(max_length=2000, null=True, blank=True)),
                ('status', models.CharField(max_length=2000, default='')),
                ('status_url', models.CharField(max_length=2000, null=True, blank=True)),
                ('launch_url', models.CharField(max_length=2000, null=True, blank=True)),
                ('orbit', models.CharField(max_length=100, null=True, blank=True)),
                ('launch_date', models.DateTimeField(null=True, verbose_name='date launched', blank=True)),
                ('launch_date_tbd', models.NullBooleanField()),
                ('created_date', models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 4, 29, 12, 14, 3, 443781))),
                ('updated_date', models.DateTimeField(null=True, verbose_name='date updated', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LaunchArticle',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=2000)),
                ('launch', models.ForeignKey(default='', to='rocketapp.Launch')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LaunchVideo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=2000)),
                ('description', models.CharField(max_length=2000)),
                ('launch', models.ForeignKey(default='', to='rocketapp.Launch')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=10)),
                ('url', models.CharField(max_length=2000)),
                ('wiki_url', models.CharField(max_length=2000)),
                ('description', models.CharField(max_length=2000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=2000)),
                ('wiki_url', models.CharField(max_length=2000)),
                ('description', models.CharField(max_length=2000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payload',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=2000)),
                ('wiki_url', models.CharField(max_length=2000)),
                ('description', models.CharField(max_length=2000)),
                ('manufacturers', models.ManyToManyField(to='rocketapp.Manufacturer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PayloadVideo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=2000)),
                ('description', models.CharField(max_length=2000)),
                ('payload', models.ForeignKey(default='', to='rocketapp.Payload')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rocket',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('stages', models.IntegerField()),
                ('height', models.DecimalField(max_digits=8, decimal_places=2)),
                ('mass', models.DecimalField(max_digits=8, decimal_places=2)),
                ('diameter', models.DecimalField(max_digits=8, decimal_places=2)),
                ('cost', models.DecimalField(max_digits=15, decimal_places=2, null=True)),
                ('cost_year', models.IntegerField(null=True)),
                ('payload_to_leo', models.DecimalField(max_digits=8, decimal_places=2, null=True)),
                ('payload_to_gto', models.DecimalField(max_digits=8, decimal_places=2, null=True)),
                ('payload_to_sso', models.DecimalField(max_digits=8, decimal_places=2, null=True)),
                ('payload_to_gso', models.DecimalField(max_digits=8, decimal_places=2, null=True)),
                ('status', models.CharField(max_length=200)),
                ('first_flight_date', models.DateTimeField(null=True, blank=True)),
                ('wiki_url', models.CharField(max_length=1000)),
                ('rocket_function', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('country', models.CharField(max_length=10)),
                ('created_date', models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 4, 29, 12, 14, 3, 442402))),
                ('updated_date', models.DateTimeField(null=True, verbose_name='date updated', blank=True)),
                ('manufacturers', models.ManyToManyField(to='rocketapp.Manufacturer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('email', models.CharField(max_length=200, default='')),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 4, 29, 12, 14, 3, 445884))),
                ('updated_date', models.DateTimeField(null=True, verbose_name='date updated', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='launch',
            name='rocket',
            field=models.ForeignKey(default='', to='rocketapp.Rocket'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rocketapp', '0002_auto_20141228_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rocket',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('stages', models.IntegerField()),
                ('height', models.DecimalField(max_digits=8, decimal_places=2)),
                ('mass', models.DecimalField(max_digits=8, decimal_places=2)),
                ('diameter', models.DecimalField(max_digits=8, decimal_places=2)),
                ('cost', models.DecimalField(max_digits=15, decimal_places=2)),
                ('cost_year', models.IntegerField()),
                ('payload_to_leo', models.DecimalField(max_digits=8, decimal_places=2)),
                ('payload_to_gto', models.DecimalField(max_digits=8, decimal_places=2)),
                ('payload_to_sso', models.DecimalField(max_digits=8, decimal_places=2)),
                ('status', models.CharField(max_length=200)),
                ('first_flight_date', models.DateTimeField(blank=True, null=True)),
                ('wiki_url', models.CharField(max_length=1000)),
                ('manufacturer_url', models.CharField(max_length=1000)),
                ('rocket_function', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('country', models.CharField(max_length=10)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2014, 12, 29, 6, 50, 20, 88737), verbose_name='date created')),
                ('updated_date', models.DateTimeField(blank=True, null=True, verbose_name='date updated')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='launch',
            name='name',
        ),
        migrations.AddField(
            model_name='launch',
            name='country',
            field=models.CharField(max_length=10, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='launch',
            name='customer',
            field=models.CharField(max_length=2000, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='launch',
            name='customer_url',
            field=models.CharField(max_length=2000, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='launch',
            name='orbit',
            field=models.CharField(max_length=100, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='launch',
            name='payload',
            field=models.CharField(max_length=2000, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='launch',
            name='remarks',
            field=models.CharField(max_length=2000, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='launch',
            name='rocket',
            field=models.ForeignKey(default='', to='rocketapp.Rocket'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='launch',
            name='status',
            field=models.CharField(max_length=2000, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='launch',
            name='status_url',
            field=models.CharField(max_length=2000, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='launch',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 29, 6, 50, 20, 89738), verbose_name='date created'),
            preserve_default=True,
        ),
    ]

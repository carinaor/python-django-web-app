# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 23:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('iso2code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('iso3code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=200)),
                ('capital', models.CharField(max_length=200)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HSProduct',
            fields=[
                ('hs_number', models.CharField(blank=True, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='IntracenImportData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imported_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('imported_time', models.PositiveSmallIntegerField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newmarkets.Country')),
                ('hs_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newmarkets.HSProduct')),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='country',
            field=models.ManyToManyField(through='newmarkets.IntracenImportData', to='newmarkets.HSProduct'),
        ),
    ]

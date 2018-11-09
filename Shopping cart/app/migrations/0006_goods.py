# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-25 02:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_foodtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=16)),
                ('productimg', models.CharField(max_length=200)),
                ('productname', models.CharField(max_length=50)),
                ('productlongname', models.CharField(max_length=100)),
                ('isxf', models.BooleanField(default=0)),
                ('pmdesc', models.IntegerField(default=0)),
                ('specifics', models.CharField(max_length=50)),
                ('price', models.FloatField(default=0)),
                ('marketprice', models.FloatField(default=0)),
                ('categoryid', models.CharField(max_length=50)),
                ('childcid', models.CharField(max_length=50)),
                ('childcidname', models.CharField(max_length=100)),
                ('dealerid', models.CharField(max_length=50)),
                ('storenums', models.IntegerField(default=0)),
                ('productnum', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'axf_goods',
            },
        ),
    ]

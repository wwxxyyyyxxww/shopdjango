# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-25 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=32, unique=True)),
                ('u_password', models.CharField(max_length=32)),
                ('u_mail', models.CharField(max_length=64, unique=True)),
                ('u_sex', models.BooleanField(default=True)),
                ('u_img', models.ImageField(upload_to='img')),
            ],
            options={
                'db_table': 'axf_user',
            },
        ),
    ]

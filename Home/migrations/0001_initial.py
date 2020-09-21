# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-09-10 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=32)),
                ('trackid', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'yxs_wheel',
            },
        ),
    ]
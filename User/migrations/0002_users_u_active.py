# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-09-16 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='u_active',
            field=models.BooleanField(default=False),
        ),
    ]

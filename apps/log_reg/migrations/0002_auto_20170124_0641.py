# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

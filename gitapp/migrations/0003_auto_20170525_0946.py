# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-25 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gitapp', '0002_auto_20170525_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gitcommit',
            name='branch',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

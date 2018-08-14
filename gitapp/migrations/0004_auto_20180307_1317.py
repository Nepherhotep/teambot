# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-07 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gitapp', '0003_auto_20170525_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gitcommit',
            name='author_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_commits', to='botapp.UserProfile'),
        ),
        migrations.AlterField(
            model_name='gitcommit',
            name='committer_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='merged_commits', to='botapp.UserProfile'),
        ),
    ]

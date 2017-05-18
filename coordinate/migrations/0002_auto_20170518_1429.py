# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='position_X',
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='position_Y',
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='public_key',
        ),
        migrations.AddField(
            model_name='transfer',
            name='ip_direct',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
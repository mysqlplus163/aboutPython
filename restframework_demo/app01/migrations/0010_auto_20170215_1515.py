# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-15 07:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0009_auto_20170215_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boss',
            name='publisher',
        ),
        migrations.DeleteModel(
            name='Boss',
        ),
    ]

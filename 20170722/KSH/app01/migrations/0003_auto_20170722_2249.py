# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20170722_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='create_time',
            field=models.TextField(auto_created=True, editable=False, verbose_name='创建时间'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-29 03:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app02.Class'),
            preserve_default=False,
        ),
    ]

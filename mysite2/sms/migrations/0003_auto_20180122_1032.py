# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-22 10:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_auto_20180122_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='the_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', related_query_name='s', to='sms.Class'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-22 10:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='the_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='sms.Class'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-22 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_auto_20180122_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='detail',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='sms.StudentDetail'),
        ),
    ]
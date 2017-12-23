# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-11 04:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20170829_0915'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HRBP_type_id', models.IntegerField(choices=[(1, '确认'), (2, '未确认')], default=1)),
            ],
            options={
                'verbose_name': 'test',
                'verbose_name_plural': 'test',
            },
        ),
    ]

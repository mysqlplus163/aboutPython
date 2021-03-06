# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-23 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20170723_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True, verbose_name='上线时间')),
                ('name', models.CharField(max_length=32, verbose_name='产品名称')),
                ('status', models.IntegerField(choices=[(0, '在计划'), (1, '已上线'), (-1, '下线了')], verbose_name='状态')),
            ],
            options={
                'verbose_name': '产品',
                'verbose_name_plural': '产品',
            },
        ),
        migrations.DeleteModel(
            name='Info',
        ),
    ]

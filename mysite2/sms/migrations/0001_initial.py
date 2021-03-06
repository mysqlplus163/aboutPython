# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-22 10:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=32, verbose_name='班级名称')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=32, verbose_name='学生姓名')),
                ('the_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='sms.Class')),
            ],
        ),
    ]

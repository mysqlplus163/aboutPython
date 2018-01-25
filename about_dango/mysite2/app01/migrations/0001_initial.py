# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-21 13:00
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
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=32)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=32)),
                ('the_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=32)),
                ('class_list', models.ManyToManyField(to='app01.Class')),
            ],
        ),
    ]
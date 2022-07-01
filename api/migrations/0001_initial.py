# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 23:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Birth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_event', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Rabbit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('FEMALE', 'F'), ('MALE', 'M')], max_length=1)),
                ('race', models.IntegerField(choices=[('NEW ZELAND', 0), ('GIANT FLANDES', 1)])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
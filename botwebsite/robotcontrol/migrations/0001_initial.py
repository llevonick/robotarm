# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos_1', models.IntegerField(default=0)),
                ('pos_2', models.IntegerField(default=0)),
                ('pos_3', models.IntegerField(default=0)),
                ('pos_4', models.IntegerField(default=0)),
                ('pos_5', models.IntegerField(default=0)),
            ],
        ),
    ]

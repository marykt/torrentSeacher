# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-31 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TorrentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('infohash', models.CharField(max_length=40)),
                ('hot1', models.IntegerField(default=0)),
                ('hot2', models.IntegerField(default=0)),
            ],
        ),
    ]

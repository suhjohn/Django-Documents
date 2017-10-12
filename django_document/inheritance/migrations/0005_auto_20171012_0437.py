# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 04:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inheritance', '0004_champion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mid',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('inheritance.champion',),
        ),
        migrations.CreateModel(
            name='Supporter',
            fields=[
            ],
            options={
                'ordering': ['name'],
                'proxy': True,
                'indexes': [],
            },
            bases=('inheritance.champion',),
        ),
        migrations.AlterModelOptions(
            name='champion',
            options={'ordering': ['rank']},
        ),
    ]

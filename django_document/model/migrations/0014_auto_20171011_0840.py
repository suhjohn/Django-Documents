# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 08:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0013_auto_20171011_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='place',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='model.Place'),
        ),
    ]
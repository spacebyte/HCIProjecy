# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hciproject', '0003_auto_20161123_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
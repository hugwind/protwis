# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-01 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0006_auto_20170901_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='structuremodel',
            name='version',
            field=models.DateField(default='2017-01-01'),
            preserve_default=False,
        ),
    ]
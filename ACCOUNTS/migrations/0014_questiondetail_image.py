# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-01 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ACCOUNTS', '0013_auto_20161031_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='questiondetail',
            name='Image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Image'),
        ),
    ]
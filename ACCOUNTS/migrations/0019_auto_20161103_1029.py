# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-03 04:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ACCOUNTS', '0018_studentdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdetail',
            name='Interests',
        ),
        migrations.RemoveField(
            model_name='studentdetail',
            name='Qualification',
        ),
    ]
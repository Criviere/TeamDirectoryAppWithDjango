# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 20:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='titles',
            new_name='title',
        ),
    ]

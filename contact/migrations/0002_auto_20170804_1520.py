# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 11:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserMessage',
            new_name='ContactForm',
        ),
    ]

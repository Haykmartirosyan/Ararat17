# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-05 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_employees'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=64)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Messages',
                'verbose_name': 'Message',
            },
        ),
    ]

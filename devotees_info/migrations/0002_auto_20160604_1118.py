# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-04 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devotees_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devoteesmaterialinfo',
            name='date_of_birth',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='devoteesmaterialinfo',
            name='phone_number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='devoteesspouseinfo',
            name='date_of_birth',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='devotesschildreninfo',
            name='date_of_birth',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]

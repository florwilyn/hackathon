# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-27 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='image',
            field=models.ImageField(null=True, upload_to='./storage/'),
        ),
    ]

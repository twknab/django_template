# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-28 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secrets', '0004_remove_secret_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='secret',
            name='likes',
            field=models.ManyToManyField(to='secrets.User'),
        ),
    ]

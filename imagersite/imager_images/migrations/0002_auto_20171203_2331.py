# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 23:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='photo',
            field=models.ManyToManyField(related_name='album', to='imager_images.Photo'),
        ),
    ]

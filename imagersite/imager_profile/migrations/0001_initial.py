# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 23:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('fee', models.FloatField(blank=True, null=True)),
                ('camera_choices', models.CharField(choices=[('CANON', 'Canon'), ('NIKON', 'Nikon'), ('OLYMPUS', 'Olyumpus')], default='CANON', max_length=50)),
                ('services_choices', models.CharField(choices=[('PORTRAIT', 'Portrait'), ('WEDDING', 'Wedding'), ('AWKWARD', 'Awkward')], default='PORTRAIT', max_length=50)),
                ('bio', models.TextField()),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('photo_styles', models.CharField(choices=[('BW', 'Black and White'), ('Color', 'Color')], default='BW', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
    ]

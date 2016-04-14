# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-14 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balderdash', '0003_userdefinition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prompt',
            name='category',
            field=models.CharField(blank=True, choices=[('Word', 'Word'), ('Movie', 'Movie'), ('Name', 'Name'), ('Acronym', 'Acronym'), ('Law', 'Law')], max_length=1, null=True),
        ),
    ]

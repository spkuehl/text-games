# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prompt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=20)),
                ('definition', models.CharField(max_length=150)),
            ],
        ),
    ]
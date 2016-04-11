# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 20:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('balderdash', '0002_prompt_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=4)),
                ('user_definition', models.CharField(max_length=150)),
                ('prompt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='balderdash.Prompt')),
                ('user_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
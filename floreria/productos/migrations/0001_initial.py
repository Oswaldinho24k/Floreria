# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='flowers')),
                ('available', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-11-16 15:01
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField(blank=True)),
                ('text', ckeditor.fields.RichTextField(blank=True)),
            ],
            options={
                'verbose_name': '\u0422\u0435\u043a\u0441\u0442 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f',
                'verbose_name_plural': '\u0422\u0435\u043a\u0441\u0442\u044b \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0439',
            },
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(blank=True, max_length=64)),
                ('date_birth', models.DateField(blank=True)),
            ],
            options={
                'verbose_name': '\u041f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u0438',
                'verbose_name_plural': '\u041f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u0438',
            },
        ),
    ]

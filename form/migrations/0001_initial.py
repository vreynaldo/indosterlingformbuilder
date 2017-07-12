# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 05:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EventDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('jsondata', models.TextField()),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Date_Create')),
                ('last_modified', models.DateField(auto_now=True, verbose_name='Last_Modified')),
                ('eventID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('responseJSON', models.TextField()),
                ('imagePath', models.TextField()),
                ('idCardPath', models.TextField()),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('eventDetailsID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.EventDetails')),
                ('eventID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.Event')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
                ('Fname', models.CharField(max_length=100)),
                ('Lname', models.CharField(max_length=100)),
                ('passHash', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.User'),
        ),
    ]
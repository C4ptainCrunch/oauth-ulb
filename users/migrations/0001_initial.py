# Generated by Django 2.0.2 on 2018-02-16 20:14

import datetime
from django.db import migrations, models
import libnetid.django.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('netid', models.CharField(max_length=20, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('raw_matricule', models.CharField(blank=True, max_length=255)),
                ('birthday', models.DateField(blank=True, default=datetime.date(1970, 1, 1))),
                ('library', models.CharField(blank=True, max_length=255)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', libnetid.django.models.LibNetidUserManager()),
            ],
        ),
    ]
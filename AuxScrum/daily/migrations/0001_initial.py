# Generated by Django 4.0.2 on 2022-04-13 13:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dateDaily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=datetime.date.today)),
                ('user', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='dateRetro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=datetime.date.today)),
                ('user', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='formularioRetro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.CharField(max_length=2500)),
                ('q2', models.CharField(max_length=2500)),
                ('q3', models.CharField(max_length=2500)),
                ('date_retro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daily.dateretro')),
            ],
        ),
        migrations.CreateModel(
            name='formularioDaily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.CharField(max_length=2500)),
                ('q2', models.CharField(max_length=2500)),
                ('q3', models.CharField(max_length=2500)),
                ('date_daily', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daily.datedaily')),
            ],
        ),
    ]

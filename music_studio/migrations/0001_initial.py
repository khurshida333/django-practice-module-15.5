# Generated by Django 5.0.6 on 2024-07-02 18:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=100)),
                ('Phone_Number', models.IntegerField(max_length=12)),
                ('Instrument_Type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Album_Name', models.CharField(max_length=50)),
                ('Album_release_date', models.DateField()),
                ('Ratings', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')])),
                ('Musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_studio.musician')),
            ],
        ),
    ]

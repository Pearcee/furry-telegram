# Generated by Django 3.1.1 on 2020-12-21 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temprature', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='sensor',
            old_name='Humidity',
            new_name='humidity',
        ),
        migrations.RenameField(
            model_name='sensor',
            old_name='Remark',
            new_name='remark',
        ),
        migrations.RenameField(
            model_name='sensor',
            old_name='Temp',
            new_name='temp',
        ),
    ]

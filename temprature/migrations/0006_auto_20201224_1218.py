# Generated by Django 3.1.1 on 2020-12-24 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temprature', '0005_auto_20201223_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='online',
            name='name',
            field=models.CharField(max_length=32),
        ),
    ]

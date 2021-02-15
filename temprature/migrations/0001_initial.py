# Generated by Django 3.1.1 on 2020-12-21 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Temp', models.DecimalField(decimal_places=2, max_digits=2)),
                ('Humidity', models.DecimalField(decimal_places=2, max_digits=2)),
                ('Date', models.DateTimeField()),
                ('Remark', models.TextField()),
            ],
        ),
    ]
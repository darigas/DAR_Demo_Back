# Generated by Django 2.2.4 on 2019-08-30 20:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kino_kz', '0010_auto_20190830_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cinema',
            name='city',
        ),
        migrations.AlterField(
            model_name='movie',
            name='premiere',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 8, 30, 20, 0, 41, 977994)),
        ),
    ]
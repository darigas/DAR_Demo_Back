# Generated by Django 2.2.4 on 2019-08-18 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kino_kz', '0002_auto_20190818_1649'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={},
        ),
        migrations.RemoveField(
            model_name='movie',
            name='country',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='duration',
        ),
        migrations.AlterField(
            model_name='movie',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
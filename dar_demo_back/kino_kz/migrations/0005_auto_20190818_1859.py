# Generated by Django 2.2.4 on 2019-08-18 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kino_kz', '0004_comingsoonmovie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('poster', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Кинотеатр',
                'verbose_name_plural': 'Кинотеатры',
            },
        ),
        migrations.CreateModel(
            name='CinemaManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='comingsoonmovie',
            options={'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
    ]

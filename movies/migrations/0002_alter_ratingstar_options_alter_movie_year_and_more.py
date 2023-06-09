# Generated by Django 4.1.7 on 2023-03-23 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['-value'], 'verbose_name': 'Звезда рейтинга', 'verbose_name_plural': 'Звезды рейтинга'},
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Дата выхода'),
        ),
        migrations.AlterField(
            model_name='ratingstar',
            name='value',
            field=models.SmallIntegerField(default=0, verbose_name='Значение'),
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-16 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_library_app', '0002_auto_20211103_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamecategories',
            name='game_categories',
            field=models.PositiveSmallIntegerField(choices=[(7, 'Towarzyskie'), (3, 'Logiczne'), (6, 'Wyścigi'), (4, 'Zręcznościowe'), (8, 'Bijatyki'), (9, 'Przygodowe'), (5, 'Strategiczne'), (10, 'Symulacje'), (1, 'RPG'), (0, 'Akcji'), (2, 'Sportowe')], default=0),
        ),
    ]

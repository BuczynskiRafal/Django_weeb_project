# Generated by Django 3.2.9 on 2021-11-03 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_library_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamecategories',
            name='game_categories',
            field=models.PositiveSmallIntegerField(choices=[(2, 'Sportowe'), (7, 'Towarzyskie'), (6, 'Wyścigi'), (4, 'Zręcznościowe'), (9, 'Przygodowe'), (0, 'Akcji'), (8, 'Bijatyki'), (5, 'Strategiczne'), (10, 'Symulacje'), (3, 'Logiczne'), (1, 'RPG')], default=0),
        ),
        migrations.AddField(
            model_name='gamemode',
            name='game_mode',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Multiplayer'), (0, 'Singleplayer')], default=0),
        ),
    ]

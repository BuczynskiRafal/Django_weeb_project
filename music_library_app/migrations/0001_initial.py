# Generated by Django 3.2.9 on 2021-11-03 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='GameMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='GameRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users_rating', models.PositiveIntegerField(default=5)),
                ('votes', models.PositiveIntegerField(default=100)),
                ('expectations_before_the_premiere', models.PositiveSmallIntegerField(default=5)),
                ('votes_before_the_premiere', models.PositiveIntegerField(default=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='game title', max_length=256, unique=True)),
                ('description', models.TextField(blank=True, default='description of the game')),
                ('creation_date', models.DateField(blank=True, default='2000-01-01')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='posters')),
                ('story', models.TextField(blank=True, default='Gra <django.db.models.fields.CharField> jest o <django.db.models.fields.TextField>')),
                ('mechanics', models.TextField(blank=True, default='Gra <django.db.models.fields.CharField> powstała jako gra <django.db.models.fields.related.OneToOneField>')),
                ('technical_issues', models.TextField(blank=True, default='sample_text')),
                ('min_hardware_requirements', models.TextField(blank=True, default='Intel Core i5-6300U 2.4 GHz 8 GB RAM karta grafiki Intel HD 520 lub lepsza 50 GB HDD Windows 10 64-bit.')),
                ('recommended_hardware_requirements', models.TextField(blank=True, default='Intel Core i5-8600K 3.6 GHz 16 GB RAM karta grafiki 4 GB GeForce GTX 970 lub lepsza 50 GB HDD Windows 10 64-bit.')),
                ('category', models.OneToOneField(default='Akcji', null=True, on_delete=django.db.models.deletion.CASCADE, to='music_library_app.gamecategories')),
                ('game_mode', models.OneToOneField(default='Singleplayer', null=True, on_delete=django.db.models.deletion.CASCADE, to='music_library_app.gamemode')),
            ],
        ),
    ]
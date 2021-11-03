from django.db import models


class GameCategories(models.Model):
    game_categories = {
        (0, "Akcji"),
        (1, "RPG"),
        (2, "Sportowe"),
        (3, "Logiczne"),
        (4, "Zręcznościowe"),
        (5, "Strategiczne"),
        (6, "Wyścigi"),
        (7, "Towarzyskie"),
        (8, "Bijatyki"),
        (9, "Przygodowe"),
        (10, "Symulacje"),
    }


class GameMode(models.Model):
    game_mode = {(0, "Singleplayer"), (1, "Multiplayer")}


class Game(models.Model):
    title = models.CharField(
        max_length=256, blank=False, unique=True, default="game title"
    )
    description = models.TextField(
        blank=True, unique=False, default="description of the game"
    )
    creation_date = models.DateField(unique=False, blank=True, default="2000-01-01")
    poster = models.ImageField(upload_to="posters", null=True, blank=True)
    # fabuła
    story = models.TextField(
        blank=True, unique=False, default=f"Gra {title} jest o {description}"
    )
    # tryb gry
    game_mode = models.OneToOneField(
        GameMode,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        default="Singleplayer",
    )
    category = models.OneToOneField(
        GameCategories,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        default=GameCategories.game_categories[0],
    )
    # mechanika
    mechanics = models.TextField(
        blank=True, unique=False, default=f"Gra {title} powstała jako gra {category}"
    )
    # Technical issues
    technical_issues = models.TextField(blank=True, unique=False, default="sample_text")
    # Hardware requirements
    min_hardware_requirements = models.TextField(
        blank=True,
        unique=False,
        default="Intel Core i5-6300U 2.4 GHz 8 GB RAM karta grafiki Intel HD 520 lub lepsza 50 GB HDD Windows 10 64-bit.",
    )
    recommended_hardware_requirements = models.TextField(
        blank=True,
        unique=False,
        default="Intel Core i5-8600K 3.6 GHz 16 GB RAM karta grafiki 4 GB GeForce GTX 970 lub lepsza 50 GB HDD Windows 10 64-bit.",
    )

    def __repr__(self):
        return f"Class {__class__.__name__} has attributes {self.__class__.__dict__}"


class GameRating(models.Model):
    users_rating = models.PositiveIntegerField(default=5)
    votes = models.PositiveIntegerField(default=100)
    expectations_before_the_premiere = models.PositiveSmallIntegerField(default=5)
    votes_before_the_premiere = models.PositiveIntegerField(default=1000)

    def game_rating_summary(self):
        summary = (
            f"Ocena użytkowników: {self.users_rating} / 10 na podstawie {self.votes} głosów czytelników."
            f"Oczekiwania czytelników przed premierą: {self.expectations_before_the_premiere} / 10 na podstawie {self.votes_before_the_premiere} głosów czytelników."
        )
        return summary

    def __repr__(self):
        return f"Class {__class__.__name__} has attributes {self.__class__.__dict__}"

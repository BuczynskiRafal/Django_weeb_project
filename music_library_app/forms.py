from django.forms import ModelForm
from .models import Game
from .models import GameMode
from .models import GameRating
from .models import GameCategories


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = [field for field in model.__dict__.keys() if not field.startswith('__')]


class GameModeForm(ModelForm):
    class Meta:
        model = GameMode
        fields = [field for field in model.__dict__.keys() if not field.startswith('__')]


class GameRatingForm(ModelForm):
    class Meta:
        model = GameRating
        fields = [field for field in model.__dict__.keys() if not field.startswith('__')]


class GameCategoriesForm(ModelForm):
    class Meta:
        model = GameCategories
        fields = [field for field in model.__dict__.keys() if not field.startswith('__')]

from django.forms import ModelForm
from .models import Game
from .models import GameMode
from .models import GameRating
from .models import GameCategories


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'description', 'creation_date', 'poster', 'story', 'game_mode', 'category', 'mechanics',
                  'technical_issues', 'min_hardware_requirements', 'recommended_hardware_requirements']

        # fields = [field for field in model.__dict__.keys() if not field.startswith('_')]


class GameModeForm(ModelForm):
    class Meta:
        model = GameMode
        fields = ['game_mode']
        # fields = [field for field in model.__dict__.keys() if not field.startswith('_')]


class GameRatingForm(ModelForm):
    class Meta:
        model = GameRating
        fields = ['users_rating', 'votes', 'expectations_before_the_premiere', 'votes_before_the_premiere']
        # fields = [field for field in model.__dict__.keys() if not field.startswith('_')]


class GameCategoriesForm(ModelForm):
    class Meta:
        model = GameCategories
        fields = ['game_categories']
        # fields = [field for field in model.__dict__.keys() if not field.startswith('_')]

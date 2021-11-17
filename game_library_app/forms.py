from django.forms import ModelForm
from .models import Game
from .models import GameMode
from .models import GameRating
from .models import GameCategories


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class GameModeForm(ModelForm):
    class Meta:
        model = GameMode
        fields = '__all__'


class GameRatingForm(ModelForm):
    class Meta:
        model = GameRating
        fields = '__all__'


class GameCategoriesForm(ModelForm):
    class Meta:
        model = GameCategories
        fields = '__all__'

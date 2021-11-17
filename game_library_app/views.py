from django.shortcuts import render
from django.template import loader
from .models import Game
from .models import GameMode
from .models import GameRating
from .models import GameCategories
from .forms import GameForm
from .forms import GameModeForm
from .forms import GameRatingForm
from .forms import GameCategoriesForm


def all_games(request):
    games = Game.objects.all()
    return render(request, 'main.html', {'games': games})


def game(request):
    games = Game.objects.all()
    return render(request, 'games/game.html', {'games': games})


def games(request):
    games = Game.objects.all()
    return render(request, 'lists/lists.html', {'games': games})

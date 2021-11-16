from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Game
from .models import GameMode
from .models import GameRating
from .models import GameCategories
from .forms import GameForm
from .forms import GameModeForm
from .forms import GameRatingForm
from .forms import GameCategoriesForm


def response_test(request):
    return HttpResponse("<h1>It is working</h1>")


def all_games(request):
    games = Game.objects.all()
    return render(request, 'main.html', {'games': games})


def game(request):
    games = Game.objects.all()
    # game = game.category
    template = loader.get_template('games/game.html')
    context = {'games': games}
    return HttpResponse(template.render(context=context))

def first_game(request):
    game = Game.objects.first()
    game = f"<h1>{game.title}</h1>" \
           f"<p>{game.category}</p."
    return HttpResponse(game)
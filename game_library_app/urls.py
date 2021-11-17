from django.urls import path
from .views import *

urlpatterns = [
    path('all', all_games, name='all_games'),
    path('game/', game, name='game'),
    path('game/1/', games, name='games'),
]
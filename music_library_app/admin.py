from django.contrib import admin

from .models import Game
from .models import GameMode
from .models import GameRating
from .models import GameCategories

admin.site.register(Game)
admin.site.register(GameMode)
admin.site.register(GameRating)
admin.site.register(GameCategories)

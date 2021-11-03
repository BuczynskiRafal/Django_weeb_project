from django.urls import path
from music_library_app.views import *

urlpatterns = [
    path('', response_test, name='response_test')
]
from django.urls import path
from .views import index, find_labyrinths, find_labyrinth_rooms

BASE_URL: str = 'api/v1/'

urlpatterns = [
    path('', index),
    path(f'{BASE_URL}labyrinths', find_labyrinths),
    path(f'{BASE_URL}labyrinths/<int:labyrinth_id>/rooms', find_labyrinth_rooms)
]

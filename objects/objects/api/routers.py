from django.urls import path
from objects.views import index, find_labyrinths, find_labyrinth_rooms
from .swagger import schema_view

BASE_URL: str = 'api/v1/'

urlpatterns = [
    path('', index),
    path(f'{BASE_URL}docs', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(f'{BASE_URL}labyrinths', find_labyrinths),
    path(f'{BASE_URL}labyrinths/<int:labyrinth_id>/rooms', find_labyrinth_rooms)
]

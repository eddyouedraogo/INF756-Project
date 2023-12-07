from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/sim/(?P<lab_name>\w+)/$', consumers.SimulationConsumer.as_asgi()),
]
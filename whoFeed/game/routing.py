from django.urls import re_path
from .consumers import TicksSyncConsumer

websocket_urlpatterns = [
    re_path(r"ws/game/(?P<party_ID>\w+)/$", TicksSyncConsumer.as_asgi()),
]

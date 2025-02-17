from django.urls import re_path
from .consumers import TicksSyncConsumer

websocket_urlpatterns = [
    re_path(r"ws/ticks/$", TicksSyncConsumer.as_asgi()),
]

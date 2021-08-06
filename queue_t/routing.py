# chat/routing.py
from django.conf.urls import re_path, url

from . import consumers

websocket_urlpatterns = [
   re_path(r'ws/queue_t$', consumers.Queue_tConsumer.as_asgi()),
]

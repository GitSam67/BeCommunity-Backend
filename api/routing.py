from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    # re_path(r"ws/api/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
]
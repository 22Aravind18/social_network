# routes the sender or reciever to chat consumer and builds the websocket url
# asgi() makes the chatconsumer class an asyncronous function to handle realtime long living connections.

from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path("ws/chat/<int:recipient_id>/", ChatConsumer.as_asgi()),
]
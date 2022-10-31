from django.urls import path

from chats.consumers.consumer import MessageConsumer
from chats.consumers.notification import NewUserConsumer

websocket_urlpatterns = [
    path('ws/notification/<str:username>/', NewUserConsumer.as_asgi()),
    path('ws/message/<str:username>/', MessageConsumer.as_asgi()),
]

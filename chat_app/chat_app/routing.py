from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import os
from chats import ws_urls
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            ws_urls.websocket_urlpatterns
        )
    )
})

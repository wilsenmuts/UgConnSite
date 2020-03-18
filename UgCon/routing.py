from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import django_chatter.routing
from . import consumers


application = ProtocolTypeRouter({
  'websocket': AuthMiddlewareStack(
    URLRouter(
    django_chatter.routing.websocket_urlpatterns # send request to chatter's urls
    )
  )
})


websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
]
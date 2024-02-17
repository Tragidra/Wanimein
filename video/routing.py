# routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from video.views import VideoConsumer

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter([
        path('ws/video_stream/<str:filename>/', VideoConsumer.as_asgi()),
    ]),
})

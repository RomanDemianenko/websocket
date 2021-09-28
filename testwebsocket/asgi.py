"""
ASGI config for examinator project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

from webtest.rounting import websockets_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testwebsocket.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": websockets_urlpatterns,
})

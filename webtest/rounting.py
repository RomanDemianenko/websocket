from channels.routing import URLRouter
from django.conf.urls import url

from webtest.consumer import TrafficLights

websockets_urlpatterns = URLRouter([
    url(
        "ws/traffic/(?P<pk>[^/]+)/", TrafficLights.as_asgi(),
        name="traffic",
    ),

])

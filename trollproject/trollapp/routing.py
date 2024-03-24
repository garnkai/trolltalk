# File handles all the asynchronous functionality
from django.urls import re_path , include
from trollapp.consumers import ChatConsumer
 
# Here, "" is routing to the URL ChatConsumer which 
# will handle the chat functionality.
websocket_urlpatterns = [
    #path('', ChatConsumer.as_asgi()),
    re_path(r'ws/(?P<websocket_id>\w+)/$', ChatConsumer.as_asgi()),
]





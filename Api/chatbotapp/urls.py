from django.urls import path
from .views import send_message, list_messages

urlpatterns = [
    path('send_message/', send_message, name='send_message'),
    path('list_messages/', list_messages, name='list_messages'),
]

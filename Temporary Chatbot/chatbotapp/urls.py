from django.urls import path
from .views import send_message, list_messages, clear_messages
from .views import send_message, list_messages
from . import views

urlpatterns = [
    path('send', send_message, name='send_message'),
    path('', list_messages, name='list_messages'),
    path('clear-messages/', clear_messages, name='clear_messages'),  # New URL for clearing chat history
    path('home/', views.home, name='home'),
    path('send-message/', views.send_message, name='send_message'),
    path('list-messages/', views.list_messages, name='list_messages'),
    path('image-to-text/', views.image_to_text, name='image_to_text'),
    path('image-and-prompt/', views.image_and_prompt_to_text, name='image_and_prompt_to_text'),  
    path('document-and-prompt/', views.document_and_prompt_to_text, name='document_and_prompt_to_text'),
    path('temp-chat/', views.temp_chat_view, name='temp_chat'),  
]

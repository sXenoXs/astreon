from django.contrib import admin
from django.urls import path
from . views import chatbot_and_upload

urlpatterns = [
  
    path('chat/',chatbot_and_upload, name='chatbot_page'),
]

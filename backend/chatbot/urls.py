from django.urls import path
from .views import ChatWithGeminiView

urlpatterns = [
    path('chat/', ChatWithGeminiView.as_view(), name='chat_with_gemini'),
    # Other URLs...
]
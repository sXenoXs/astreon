from pathlib import Path
from .models import ChatMessage
from chatbotapp.models import ChatMessage
from chatbot.settings import GENERATIVE_AI_KEY
from django.shortcuts import redirect, render
from django.core.files.base import ContentFile
from django.conf import settings 
from django.core.files.storage import default_storage
import google.generativeai as genai
import os



def send_message(request):
    if request.method == 'POST':
        genai.configure(api_key=GENERATIVE_AI_KEY)
        model = genai.GenerativeModel("gemini-pro")

        # Handle text message
        user_message = request.POST.get('user_message')
        bot_response_text = ""

        # Initialize list to store image descriptions
        image_descriptions = []

        # Check if files are uploaded
        if 'images' in request.FILES:
            # Iterate through each uploaded file
            for image in request.FILES.getlist('images'):
                # Save each image temporarily
                path = default_storage.save(image.name, ContentFile(image.read()))
                tmp_file_path = os.path.join(settings.MEDIA_ROOT, path)

                # Delete the temporary file
                default_storage.delete(path)

            # Combine all image descriptions
            bot_response_text = " ".join(image_descriptions)

        # Generate text-based bot response if no images
        if user_message:
            bot_response = model.generate_content(user_message)
            bot_response_text += bot_response.text

        # Save message in the database
        ChatMessage.objects.create(user_message=user_message, bot_response=bot_response_text)

    return redirect('list_messages')

def upload_image_to_gemini(image_path):
    genai.configure(api_key='GENERATIVE_AI_KEY')
    model = genai.GenerativeModel("gemini-pro")
    response = model.upload_image(image_path, "image/png")
    return response.file_uri

def generate_description_from_image(file_uri):
    
    genai.configure(api_key='GENERATIVE_AI_KEY')
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(file_uri)
    return response.text

def list_messages(request):
    messages = ChatMessage.objects.all()
    return render(request, 'chatbot/list_messages.html', { 'messages': messages })
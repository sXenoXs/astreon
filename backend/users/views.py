from django.shortcuts import render, redirect
from dj_rest_auth.views import LoginView
from .serializers import CustomLoginSerializer
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .forms import ImageUploadForm, DocumentUploadForm, SingleFileUploadForm
from .models import ChatMessage, UploadedImage, UploadedDocument, UploadedFile
from mimetypes import guess_type
from django import forms
from django.conf import settings
from django.http import HttpResponse
from django.utils import timezone
import PIL
import google.generativeai as genai
import requests
import re
import os
import time

# Create your views here.

# Custom login view
def account_inactive_view(request):
    return render(request, 'account_inactive.html', {"message": "Your account is inactive."})

# Custom login view
def verification_complete(request):
    return render(request, 'verification_complete.html')

# Custom login view
class CustomLoginView(LoginView):
    serializer_class = CustomLoginSerializer




# Define the home view
def home(request):
    return HttpResponse("Welcome to the chatbot home page.")

# Define the send message view [list_messages.html]
def send_message(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message')
        
        # Configure the Gemini API
        genai.configure(api_key=settings.GENERATIVE_AI_KEY)
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 256,  # Adjust as needed
        }

        try:
            # Create a Generative Model instance
            model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                generation_config=generation_config,
            )

            # Generate a response based on the user message
            bot_response = model.generate_content(user_message).text
        except Exception as e:
            print(f"Error interacting with Gemini API: {e}")
            bot_response = "I'm sorry, I couldn't process your request at the moment."

        # Save the interaction in the database
        ChatMessage.objects.create(user_message=user_message, bot_response=bot_response)

    return redirect('list_messages')

# Define the list messages view [list_messages.html]
def list_messages(request):
    
    messages = ChatMessage.objects.all()
    return render(request, 'chatbot/list_messages.html', {'messages': messages})

# Define the clear messages view [list_messages.html]
def clear_messages(request):
    """
    Deletes all chat history from the database.
    """
    if request.method == "POST":
        # Delete all ChatMessage objects from the database
        ChatMessage.objects.all().delete()
        UploadedImage.objects.all().delete()
        UploadedDocument.objects.all().delete()
        return redirect('list_messages')  # Redirect back to the chat history page


# Configure Gemini API
genai.configure(api_key=settings.GENERATIVE_AI_KEY)

# Define a function to upload a file to Gemini
def upload_to_gemini(path, mime_type=None):
    """
    Uploads the given file to Gemini and returns the file URI.
    """
    try:
        file = genai.upload_file(path, mime_type=mime_type)
        print(f"Uploaded file '{file.display_name}' as: {file.uri}")
        return file
    except Exception as e:
        print(f"Error uploading file to Gemini: {e}")
        return None

# Define the image to text view [image_to_text.html]
def image_to_text(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded image
            uploaded_image = form.save(commit=False)
            uploaded_image.uploaded_at = timezone.now()
            uploaded_image.save()

            image_path = uploaded_image.image.path

            # Upload the image to Gemini
            gemini_file = upload_to_gemini(image_path, mime_type="image/jpeg")
            if not gemini_file:
                extracted_text = "Error uploading the image to Gemini."
            else:
                # Create a chat session with the Gemini model
                generation_config = {
                    "temperature": 1,
                    "top_p": 0.95,
                    "top_k": 40,
                    "max_output_tokens": 8192,
                    "response_mime_type": "text/plain",
                }

                model = genai.GenerativeModel(
                    model_name="gemini-1.5-flash",
                    generation_config=generation_config,
                )

                try:
                    # Start a chat with the uploaded image and prompt
                    chat_session = model.start_chat(
                        history=[
                            {
                                "role": "user",
                                "parts": [
                                    gemini_file,  # Uploaded image
                                    "What does this image say?",
                                ],
                            }
                        ]
                    )

                    # Use a valid, non-empty prompt
                    response = chat_session.send_message("Extract the text content from this image.")
                    
                    extracted_text = response.text or "No text found in the image."
                except Exception as e:
                    print(f"Error interacting with Gemini API: {e}")
                    extracted_text = "An error occurred while processing the image with Gemini."

            # Save the extracted text to the database
            uploaded_image.extracted_text = extracted_text
            uploaded_image.save()

            return render(request, 'chatbot/image_to_text_result.html', {
                'image': uploaded_image,
                'extracted_text': extracted_text,
            })
    else:
        form = ImageUploadForm()

    return render(request, "chatbot/image_to_text.html", {"form": form})

# Define the image and prompt to text view [image_and_prompt.html]
def image_and_prompt_to_text(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save(commit=False)
            uploaded_image.uploaded_at = timezone.now()
            uploaded_image.save()

            image_path = uploaded_image.image.path
            user_prompt = request.POST.get('prompt', '')

            # Upload to Gemini
            gemini_file = upload_to_gemini(image_path, mime_type="image/jpeg")
            if not gemini_file:
                bot_response = "Error uploading the image to Gemini."
            else:
                try:
                    chat_session = genai.GenerativeModel(
                        model_name="gemini-1.5-flash",
                        generation_config={
                            "temperature": 1,
                            "top_p": 0.95,
                            "top_k": 40,
                            "max_output_tokens": 8192,
                            "response_mime_type": "text/plain",
                        },
                    ).start_chat(
                        history=[
                            {
                                "role": "user",
                                "parts": [gemini_file, user_prompt],
                            }
                        ]
                    )

                    gemini_response = chat_session.send_message(user_prompt)
                    bot_response = gemini_response.text or "No text found in the image."
                except Exception as e:
                    print(f"Error interacting with Gemini API: {e}")
                    bot_response = "An error occurred while processing the image with Gemini."

            # Save chat history in the database
            ChatMessage.objects.create(user_message=user_prompt, bot_response=bot_response)

            # Save extracted text in the image model
            uploaded_image.extracted_text = bot_response
            uploaded_image.save()

            return render(request, 'chatbot/image_and_prompt_result.html', {
                'image': uploaded_image,
                'extracted_text': bot_response,
            })
    else:
        form = ImageUploadForm()

    return render(request, "chatbot/image_and_prompt.html", {"form": form})

# Define the document and prompt to text view [document_and_prompt.html]
def document_and_prompt_to_text(request):
    if request.method == "POST":
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_document = form.save(commit=False)
            uploaded_document.uploaded_at = timezone.now()
            uploaded_document.save()

            document_path = uploaded_document.document.path
            user_prompt = form.cleaned_data.get('prompt', '')

            # Upload to Gemini
            gemini_file = upload_to_gemini(document_path, mime_type="application/pdf")
            if not gemini_file:
                bot_response = "Error uploading the document to Gemini."
            else:
                try:
                    chat_session = genai.GenerativeModel(
                        model_name="gemini-1.5-flash",
                        generation_config={
                            "temperature": 1,
                            "top_p": 0.95,
                            "top_k": 40,
                            "max_output_tokens": 8192,
                            "response_mime_type": "text/plain",
                        },
                    ).start_chat(
                        history=[
                            {
                                "role": "user",
                                "parts": [gemini_file, user_prompt],
                            }
                        ]
                    )

                    gemini_response = chat_session.send_message(user_prompt)
                    bot_response = gemini_response.text or "No text found in the document."
                except Exception as e:
                    print(f"Error interacting with Gemini API: {e}")
                    bot_response = "An error occurred while processing the document with Gemini."

            # Save chat history in the database
            ChatMessage.objects.create(user_message=user_prompt, bot_response=bot_response)

            # Save extracted text in the document
            uploaded_document.extracted_text = bot_response
            uploaded_document.save()

            return render(request, 'chatbot/document_and_prompt_result.html', {
                'document': uploaded_document,
                'extracted_text': bot_response,
            })
    else:
        form = DocumentUploadForm()

    return render(request, "chatbot/document_and_prompt.html", {"form": form})

def document_and_prompt_to_text(request):
    if request.method == "POST":
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_document = form.save(commit=False)
            uploaded_document.uploaded_at = timezone.now()
            uploaded_document.save()

            document_path = uploaded_document.document.path
            user_prompt = form.cleaned_data.get('prompt', '')

            # Upload to Gemini
            gemini_file = upload_to_gemini(document_path, mime_type="application/pdf")
            if not gemini_file:
                bot_response = "Error uploading the document to Gemini."
            else:
                try:
                    chat_session = genai.GenerativeModel(
                        model_name="gemini-1.5-flash",
                        generation_config={
                            "temperature": 1,
                            "top_p": 0.95,
                            "top_k": 40,
                            "max_output_tokens": 8192,
                            "response_mime_type": "text/plain",
                        },
                    ).start_chat(
                        history=[
                            {
                                "role": "user",
                                "parts": [gemini_file, user_prompt],
                            }
                        ]
                    )

                    gemini_response = chat_session.send_message(user_prompt)
                    bot_response = gemini_response.text or "No text found in the document."
                except Exception as e:
                    print(f"Error interacting with Gemini API: {e}")
                    bot_response = "An error occurred while processing the document with Gemini."

            # Save chat history in the database
            ChatMessage.objects.create(user_message=user_prompt, bot_response=bot_response)

            # Save extracted text in the document
            uploaded_document.extracted_text = bot_response
            uploaded_document.save()

            return render(request, 'chatbot/document_and_prompt_result.html', {
                'document': uploaded_document,
                'extracted_text': bot_response,
            })
    else:
        form = DocumentUploadForm()

    return render(request, "chatbot/document_and_prompt.html", {"form": form})

# Define the save_uploaded_files function  [temp_chat.html]
def save_uploaded_files(files):
    """
    Save uploaded files to the correct directory based on type.
    """
    saved_files = []
    for file in files:
        mime_type, _ = guess_type(file.name)
        if mime_type and mime_type.startswith('image/'):
            file_type = 'image'
        else:
            file_type = 'document'

        uploaded_file = UploadedFile.objects.create(
            file=file,
            file_type=file_type,
            uploaded_at=timezone.now(),
        )
        saved_files.append(uploaded_file)

    return saved_files

# Define the wait_for_files_active function  [temp_chat.html]
def wait_for_files_active(files):
    """
    Polls the Gemini API until all files are active.
    """
    print("Waiting for file processing...")
    for file in files:
        gemini_file = genai.get_file(file.name)
        while gemini_file.state.name == "PROCESSING":
            print(".", end="", flush=True)
            time.sleep(10)
            gemini_file = genai.get_file(file.name)
        if gemini_file.state.name != "ACTIVE":
            raise Exception(f"File {file.name} failed to process")
    print("...all files ready")

# Define the handle_uploaded_file function  [temp_chat.html]
def handle_uploaded_file(uploaded_file, folder):
    """
    Save the uploaded file to the appropriate folder and return the file instance.
    """
    if folder == "images":
        # Save the file to 'media/images' and create an UploadedImage instance
        uploaded_image = UploadedImage(image=uploaded_file)
        uploaded_image.save()  # Save to database
        return uploaded_image  # Return the saved image instance
    elif folder == "documents":
        # Save the file to 'media/documents' and create an UploadedDocument instance
        uploaded_document = UploadedDocument(document=uploaded_file)
        uploaded_document.save()  # Save to database
        return uploaded_document  # Return the saved document instance
    else:
        raise ValueError("Unsupported folder type")

# Define the process_chat function [temp_chat.html]
def process_file_and_prompt(uploaded_file, prompt, file_type="file"):
    response = {"prompt": prompt, "file_name": None, "content": None, "file_type": None, "image_url": None, "document_url": None}

    if uploaded_file:
        # Determine file type and set mime type accordingly
        if file_type == "image":
            mime_type = "image/jpeg"  # For image files (JPEG)
            response["file_type"] = "image"
            response["image_url"] = uploaded_file.image.url  # Access the image's URL attribute
            response["file_name"] = uploaded_file.image.name  # Access the image's file name
        elif file_type == "document":
            mime_type = "application/pdf"  # For document files (PDF)
            response["file_type"] = "document"
            response["document_url"] = uploaded_file.document.url  # Access the document's URL attribute
            response["file_name"] = uploaded_file.document.name  # Access the document's file name
        else:
            mime_type = "application/octet-stream"  # Generic MIME type for other files
        
        # Upload the file to Gemini (upload_to_gemini is assumed to be defined)
        if file_type == "image":
            gemini_file = upload_to_gemini(uploaded_file.image.path, mime_type)  # Use image's path for upload
        elif file_type == "document":
            gemini_file = upload_to_gemini(uploaded_file.document.path, mime_type)  # Use document's path for upload

        if gemini_file:
            # Start chat with Gemini API
            try:
                chat_session = genai.GenerativeModel(model_name="gemini-1.5-flash").start_chat(
                    history=[{"role": "user", "parts": [gemini_file, prompt]}]
                )
                gemini_response = chat_session.send_message(prompt or "Process this file.")
                response["content"] = format_gemini_response(gemini_response.text) or "No content extracted."
            except Exception as e:
                print(f"Error interacting with Gemini API: {e}")
                response["content"] = "Error during Gemini API interaction."
        else:
            response["content"] = "Error uploading file to Gemini."
    
    else:
        # Handle prompt-only responses
        try:
            chat_session = genai.GenerativeModel(model_name="gemini-1.5-flash").start_chat(
                history=[{"role": "user", "parts": [prompt]}]
            )
            gemini_response = chat_session.send_message(prompt or "Provide a response.")
            response["content"] = format_gemini_response(gemini_response.text) or "No response generated."
        except Exception as e:
            print(f"Error interacting with Gemini API: {e}")
            response["content"] = "Error during Gemini API interaction."

    return response

# Define the temp_chat function [temp_chat.html]
def temp_chat_view(request):
    if request.method == "POST":
        form = SingleFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            prompt = form.cleaned_data.get("prompt", "")
            uploaded_file = request.FILES.get("file")
            bot_response = ""

            if uploaded_file:
                file_extension = uploaded_file.name.split(".")[-1].lower()
                if file_extension in ["jpg", "jpeg", "png", "gif", "webp", "heic", "heif", "jfif"]:
                    file_path = handle_uploaded_file(uploaded_file, "images")
                    response = process_file_and_prompt(file_path, prompt, file_type="image")
                    bot_response = response["content"]
                elif file_extension in ["pdf", "txt", "docx", "csv", "html", "css", "md", "xml", "rft"]:
                    file_path = handle_uploaded_file(uploaded_file, "documents")
                    response = process_file_and_prompt(file_path, prompt, file_type="document")
                    bot_response = response["content"]
                else:
                    bot_response = f"Unsupported file type: {file_extension}"
            else:
                response = process_file_and_prompt(None, prompt, file_type="prompt")
                bot_response = response["content"]

            # Save prompt and response to the database
            ChatMessage.objects.create(user_message=prompt, bot_response=bot_response)

            return render(request, "chatbot/temp_chat.html", {
                "form": form,
                "response": response,
            })
    else:
        form = SingleFileUploadForm()

    return render(request, "chatbot/temp_chat.html", {"form": form})

# Define the format_gemini_response function[temp_chat.html]
def format_gemini_response(text):
    """Format the response from Gemini for better readability."""
    
    # Add some basic formatting to the response

    # Handle unordered lists (markdown syntax "* " at the beginning of lines)
    formatted_text = re.sub(r"(^|\n)\* (.*?)($|\n)", r"\1<ul><li>\2</li></ul>", text)

    # Handle bold text (markdown syntax "**bold**")
    formatted_text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", formatted_text)

    # Handle italic text (markdown syntax "*italic*")
    formatted_text = re.sub(r"\*(.*?)\*", r"<em>\1</em>", formatted_text)

    # Handle headings (markdown syntax "# Heading")
    formatted_text = re.sub(r"(^|\n)(#{1,6})(.*?)($|\n)", r"\1<h\2>\3</h\2>", formatted_text)

    # Convert newline characters to <br> for line breaks
    formatted_text = formatted_text.replace("\n", "<br>")
    
    return formatted_text

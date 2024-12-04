from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import ChatMessageSerializer
import google.generativeai as genai
from users.models import Prompt,CustomUser
import markdown2
import os
from pathlib import Path
import json
import bleach


import logging

logger = logging.getLogger(__name__)


def clean_html(content):
    return bleach.clean(content, tags=[], strip=True)

class ChatWithGeminiView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChatMessageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_message = serializer.validated_data.get("message")
        files = request.FILES.getlist("files") 
        user = request.user 

        # Add logging to debug the user information
        logger.debug(f"Current user: {user}")
        logger.debug(f"User ID: {user.id}, Username: {user.username}")
        logger.debug(f"Request Headers: {request.headers}") 
        logger.debug(f"Request Cookies: {request.COOKIES}")

        response = self.call_gemini_api(user_message, files, user)
        return Response(response, status=status.HTTP_200_OK)


    def generate_data(self, message, result):
        data_to_save = {
            "input_message": message,
            "generated_text": result,
            "metadata": {
                "response_time": "N/A",
                "word_count": len(result.split()),
                "tokens_used": 0
            }
        }
        file_path = Path("data.json")
        with file_path.open("w") as json_file:
            json.dump(data_to_save, json_file, indent=4)

    def save_prompt_to_db(self, user_prompt, response, user):
        if self.request.user.is_authenticated:
            try:
                clean_response = clean_html(response)
                prompt = Prompt(
                    user=user,
                    user_prompt=user_prompt,
                    bot_response=clean_response
                )
                prompt.save()
                logger.debug("Prompt saved successfully!")
            except Exception as e:
                logger.error(f"Error saving prompt: {e}")
        else:
            return {"result": "error", "error_message": "User is not authenticated", "status": "failed"}

    def call_gemini_api(self, message, files, user):
        google_api_key = os.getenv("API_KEY")
        genai.configure(api_key=google_api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")

        uploaded_files = []
        for file in files:
            temp_path = Path(f"/tmp/{file.name}")
            with temp_path.open("wb") as temp_file:
                for chunk in file.chunks():
                    temp_file.write(chunk)

            uploaded_file = genai.upload_file(temp_path)
            uploaded_files.append(uploaded_file)

        try:
            result = model.generate_content(
                [*uploaded_files, "\n\n", message]
            )
            result_text = markdown2.markdown(result.text)
            self.generate_data(message, result_text)
            self.save_prompt_to_db(message, result_text, user)

            return {"result": "success", "text": result_text}

        except Exception as e:
            error_data = {
                "result": "error",
                "error_message": str(e),
                "status": "failed"
            }
            return error_data

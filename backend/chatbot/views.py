from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import ChatMessageSerializer
import google.generativeai as genai
import markdown2
import os
from pathlib import Path
import json


class ChatWithGeminiView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ChatMessageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_message = serializer.validated_data.get("message")
        files = request.FILES.getlist("files")  

        response = self.call_gemini_api(user_message, files)
        return Response(response, status=status.HTTP_200_OK)

    def generate_data(self, message, result):
        """
        This function saves the message and result into a data.json file.
        """
        data_to_save = {
            "input_message": message,
            "generated_text": result,
            "metadata": {
                "response_time": "N/A",  # Add appropriate response time if needed
                "word_count": len(result.split()),
                "tokens_used": 0  # You can add token usage if needed
            }
        }

        # Define the path where the JSON file will be saved
        file_path = Path("data.json")  # Save this file in your project directory

        # Open the file in write mode, create if it doesn't exist
        with file_path.open("w") as json_file:
            json.dump(data_to_save, json_file, indent=4)

    def call_gemini_api(self, message, files):
        # Set up genai with the API key
        google_api_key = os.getenv("API_KEY")
        genai.configure(api_key=google_api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Prepare file uploads
        uploaded_files = []
        for file in files:
            # Save the uploaded file temporarily
            temp_path = Path(f"/tmp/{file.name}")
            with temp_path.open("wb") as temp_file:
                for chunk in file.chunks():
                    temp_file.write(chunk)

            # Upload the file to Gemini
            uploaded_file = genai.upload_file(temp_path)
            uploaded_files.append(uploaded_file)

        # Generate content
        try:
            result = model.generate_content(
                [*uploaded_files, "\n\n", message]
            )

            # Convert the result to markdown (if needed)
            result_text = markdown2.markdown(result.text)

            # Save the data to data.json
            self.generate_data(message, result_text)

            # Return success response with markdown text
            return {"result": "success", "text": result_text}

        except Exception as e:
            # Handle error and return error response in JSON format
            error_data = {
                "result": "error",
                "error_message": str(e),
                "status": "failed"
            }
            return error_data

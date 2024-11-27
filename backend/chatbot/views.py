from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import ChatMessageSerializer
import google.generativeai as genai
import os
from pathlib import Path

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
            return {"result": "success", "text": result.text}
        except Exception as e:
            return {"result": "error", "message": str(e)}

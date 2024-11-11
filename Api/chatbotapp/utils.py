from django.conf import settings
import genai

def upload_image_to_gemini(image_path):
    genai.configure(api_key=settings.GENERATIVE_AI_KEY)
    model = genai.GenerativeModel("gemini-pro")
    response = model.upload_image(image_path, "image/jpeg")
    return response.file_uri

def generate_description_from_image(file_uri):
    genai.configure(api_key=settings.GENERATIVE_AI_KEY)
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(file_uri)
    return response.text

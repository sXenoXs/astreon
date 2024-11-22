
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadFileForm
from .services.process_file import extract_file_content
from .services.convert_to_json import answer_question, process_user_file, qa_pipeline
import os
import json
from django.conf import settings

# Set the uploads directory
uploads_dir = os.path.join(settings.BASE_DIR, 'uploads')
os.makedirs(uploads_dir, exist_ok=True)

def save_interactions_to_file(interactions):
    file_path = os.path.join(settings.BASE_DIR, 'chat_interactions.json')
    with open(file_path, 'w') as f:
        json.dump(interactions, f, indent=4)


def chatbot_and_upload(request):
    # Initialize an empty list to hold interactions
    if 'chat_interactions' not in request.session:
        request.session['chat_interactions'] = []

    if request.method == "POST":
        # Handle file upload
        if 'file' in request.FILES:
            file = request.FILES['file']
            temp_path = os.path.join(uploads_dir, file.name)

            # Save the uploaded file temporarily
            with open(temp_path, "wb") as f:
                for chunk in file.chunks():
                    f.write(chunk)

            # Extract file content and store it in the session
            try:
                extracted_content = extract_file_content(temp_path)
                request.session['file_content'] = extracted_content
                return JsonResponse({"message": "File uploaded and processed successfully!"})
            except Exception as e:
                return JsonResponse({"error": f"Failed to process file: {str(e)}"}, status=500)

        # Handle chatbot question
        elif 'question' in request.POST:
            question = request.POST.get('question')
            if not question:
                return JsonResponse({"message": "Please provide a valid question."}, status=400)

            # Check if file content is available
            file_content = request.session.get('file_content', None)
            if not file_content:
                return JsonResponse({"message": "No file uploaded yet. Please upload a file first."}, status=400)

            # Generate answer
            try:
                context = process_user_file(file_content)
                response = answer_question(context, question, qa_pipeline)

                # Save interaction to session
                interaction = {
                    "question": question,
                    "answer": response['answer']
                }
                chat_interactions = request.session['chat_interactions']
                chat_interactions.append(interaction)
                request.session['chat_interactions'] = chat_interactions
                request.session.modified = True  # Ensure session is updated

                save_interactions_to_file(chat_interactions)
                # Return chatbot response
                return JsonResponse({"answer": response['answer'], "message": "Chatbot response provided."})
            except Exception as e:
                return JsonResponse({"error": f"Failed to generate answer: {str(e)}"}, status=500)

    # Render the combined chatbot and upload page
    form = UploadFileForm()
    return render(request, 'ChatBot.html', {'form': form})

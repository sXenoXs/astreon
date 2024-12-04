from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token
from dj_rest_auth.views import LoginView
from .serializers import CustomLoginSerializer
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from mimetypes import guess_type
from django import forms
from django.conf import settings
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import ensure_csrf_cookie
from dj_rest_auth.views import LoginView
from .auth_backends import UsernameOrEmailBackend  # Import your custom backend
import PIL
from rest_framework.views import APIView
from django.middleware.csrf import get_token
from django.http import JsonResponse

# Create your views here.

# Custom login view
def account_inactive_view(request):
    return render(request, 'account_inactive.html', {"message": "Your account is inactive."})


def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})

# Custom login view
def verification_complete(request):
    return render(request, 'verification_complete.html')

# Custom login viewclass CustomLoginView(LoginView):
class CustomLoginView(LoginView):
    serializer_class = CustomLoginSerializer

    def post(self, request, *args, **kwargs):
        print("Received CSRF Token:", request.headers.get('X-CSRFToken'))  # Log CSRF token
        print("Received request data:", request.data)  # Debug received data

        username = request.data.get('username')
        password = request.data.get('password')

        print(f"Username: {username}, Password: {password}")  # Add this for debugging

        user = authenticate(username=username, password=password)

        if user is not None:
            if not user.is_active:  # Check if the user is inactive
                return Response({"detail": "This account has been deactivated."}, status=status.HTTP_400_BAD_REQUEST)
            print(f"Authenticating with backend: {user.backend}")  # Debug the backend
            login(request, user, backend='yourapp.auth_backends.UsernameOrEmailBackend')

            #creates a token for user authentication
            token,_ = Token.objects.get_or_create(user=user)
            return Response(
                           {"token": token.key}, 
                            status=status.HTTP_200_OK)
        else:
            print("Authentication failed")  # Add this line to check if the credentials are wrong
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)



class CustomProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({"message":f"Hello, {request.user}"})
        return Response({"message": "Not logged in"})

@csrf_protect  # Ensure CSRF protection is enabled for this view
def custom_logout(request):
    csrf_token = request.headers.get('X-CSRFToken')
    print(f"Received CSRF Token: {csrf_token}")  # Log the received CSRF token
    if not csrf_token:
        return JsonResponse({"error": "CSRF token missing or invalid"}, status=400)
    """
    Custom logout view to handle user logout with CSRF token.
    """
    if request.method == "POST":
        # Log out the user
        logout(request)

        # Send a success response
        return JsonResponse({"message": "Successfully logged out"}, status=200)
    else:
        return JsonResponse({"detail": "Method not allowed"}, status=405)



# Define the home view
def home(request):
    return HttpResponse("Welcome to the chatbot home page.")

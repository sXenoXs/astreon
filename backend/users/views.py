from django.shortcuts import render
from dj_rest_auth.views import LoginView
from .serializers import CustomLoginSerializer
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

def account_inactive_view(request):
    return render(request, 'account_inactive.html', {"message": "Your account is inactive."})

def verification_complete(request):
    return render(request, 'verification_complete.html')

class CustomLoginView(LoginView):
    serializer_class = CustomLoginSerializer

from rest_framework import serializers
from .models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = {'pk', 'email', 'username', 'email_verified', 'role_id'}
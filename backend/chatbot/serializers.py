from rest_framework import serializers
from .models import UserFile

class UserFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFile
        fields = ('file','uploaded_at')




class ChatMessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=255)
    files = serializers.ListField(child=serializers.FileField(required=False, allow_null=True),
    required=False, allow_empty=True)
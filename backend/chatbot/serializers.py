from rest_framework import serializers
from .models import UserFile

class UserFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFile
        fields = ('file','uploaded_at')




class ChatMessageSerializer(serializers.Serializer):
    message = serializers.CharField()
    files = serializers.ListField(child=serializers.FileField(required=False, allow_null=True),
    required=False, allow_empty=True)

class VerifyEmailSerializer(serializers.Serializer):
    """
    Serializer for verifying the email confirmation key.
    """
    key = serializers.CharField(max_length=64, required=True)

    def validate_key(self, value):
        if not value:
            raise serializers.ValidationError(_("This field is required."))
        return value

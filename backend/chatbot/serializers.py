from rest_framework import serializers

class VerifyEmailSerializer(serializers.Serializer):
    """
    Serializer for verifying the email confirmation key.
    """
    key = serializers.CharField(max_length=64, required=True)

    def validate_key(self, value):
        if not value:
            raise serializers.ValidationError(_("This field is required."))
        return value

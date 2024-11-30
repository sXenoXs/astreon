from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation
from dj_rest_auth.serializers import LoginSerializer
from allauth.account.models import EmailAddress
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class CustomLoginSerializer(LoginSerializer):
    # Override the username field to make it required and handle email/username
    username = serializers.CharField(required=True)
    email = None  # Remove email field from parent class

    def get_auth_user_using_orm(self, username, password):
        # Allow login using either email or username
        from django.contrib.auth import authenticate
        return authenticate(username=username, password=password)

    def validate_username(self, value):
        """
        Validate if the provided value is a username or email and return the corresponding user.
        """
        value = value.lower().strip()  # Normalize input

        if '@' in value:
            # Email validation
            try:
                user = User.objects.get(email__iexact=value)
            except User.DoesNotExist:
                raise serializers.ValidationError({
                    "username": _("No account found with this email address.")
                })
        else:
            # Username validation
            try:
                user = User.objects.get(username__iexact=value)
            except User.DoesNotExist:
                raise serializers.ValidationError({
                    "username": _("No account found with this username.")
                })

        # Check if the user is active
        if not user.is_active:
            raise serializers.ValidationError({
                "username": _("This account has been deactivated.")
            })

        self.user = user
        return value

    def validate(self, attrs):
        """
        Validate the password and return the validated attributes.
        """
        password = attrs.get('password')
        
        if not password:
            raise serializers.ValidationError({
                "password": _("Password is required.")
            })

        if not self.user.check_password(password):
            raise serializers.ValidationError({
                "password": _("Invalid password.")
            })

        # Add the user to the validated attributes
        attrs['user'] = self.user
        return attrs

class UserProfileSerializer(serializers.ModelSerializer):
    email_verified = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'email_verified', 'role_id', 'date_joined', 'last_login')
        read_only_fields = ('id', 'email_verified', 'date_joined', 'last_login')

    def get_email_verified(self, obj):
        """
        Check if the user's email is verified using allauth's EmailAddress model.
        """
        try:
            email_address = EmailAddress.objects.get_for_user(obj, obj.email)
            return email_address.verified
        except EmailAddress.DoesNotExist:
            return False

    def to_representation(self, instance):
        """
        Remove sensitive fields based on the request context.
        """
        data = super().to_representation(instance)
        request = self.context.get('request')
        
        # If not the user's own profile and not an admin
        if request and request.user != instance and not request.user.is_staff:
            # Remove sensitive fields for other users
            sensitive_fields = {'email', 'role_id', 'last_login'}
            for field in sensitive_fields:
                data.pop(field, None)
                
        return data

class CustomRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password_confirm']
        extra_kwargs = {
            'email': {'required': True},
            'username': {'required': True}
        }

    def validate_email(self, value):
        """
        Validate email format and uniqueness.
        """
        value = value.lower().strip()
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError(_("This email address is already registered."))
        return value

    def validate_username(self, value):
        """
        Validate username format and uniqueness.
        """
        value = value.strip()
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError(_("This username is already taken."))
        return value

    def validate_password(self, value):
        """
        Validate password using Django's password validation.
        """
        try:
            password_validation.validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(list(e.messages))
        return value

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        # Authenticate using either username or email
        user = self.get_auth_user_using_orm(username, password)

        if user is None:
            raise serializers.ValidationError({
                "non_field_errors": _("Unable to log in with provided credentials.")
            })

        if not user.is_active:
            raise serializers.ValidationError({
                "non_field_errors": _("User account is deactivated.")
            })

        attrs['user'] = user
        return attrs


    def create(self, validated_data):
        """
        Create a new user instance.
        """
        # Remove password_confirm from validated data
        validated_data.pop('password_confirm', None)
        
        # Create user instance
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )

        return user
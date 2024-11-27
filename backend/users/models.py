from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.timezone import now
from datetime import timedelta

class RoleType(models.TextChoices):
    ADMIN = 'admin'
    STUDENT = 'student'
    TEACHER = 'teacher'

class Role(models.Model):
    roleName = models.CharField(max_length=50, choices=RoleType.choices, default=RoleType.STUDENT)
    description = models.TextField()
    
    def __str__(self):
        return self.roleName

class TimeLog(models.Model):
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(auto_now=True)

def get_default_verification_expiration():
    return now() + timedelta(days=3)

class CustomUser(AbstractUser):
    is_verified = models.BooleanField(default=False)
    verification_expiration_date = models.DateTimeField(default=get_default_verification_expiration)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True
    )

class EmailVerification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    primary = models.BooleanField(default=False)
    expiration_date = models.DateTimeField(default=get_default_verification_expiration)

    class Meta:
        unique_together = [['user', 'email']]

    def __str__(self):
        return f"{self.email} ({self.user.username})"

class ChatMessage(models.Model):
    user_message = models.TextField(blank=True, null=True)
    bot_response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user_message}, Bot: {self.bot_response}"

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    extracted_text = models.TextField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp when the image is uploaded

    def __str__(self):
        return f"Image {self.id} - Extracted Text: {self.extracted_text[:30]}"

class UploadedDocument(models.Model):
    document = models.FileField(upload_to='documents/')  # Store in the 'documents' folder
    extracted_text = models.TextField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp when the document is uploaded

    def __str__(self):
        return f"Document {self.id} - Extracted Text: {self.extracted_text[:30]}"
    
class UploadedFile(models.Model):
    FILE_TYPES = [
        ('image', 'Image'),
        ('document', 'Document'),
    ]
    file = models.FileField(upload_to='uploads/')
    file_type = models.CharField(max_length=10, choices=FILE_TYPES)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file_type.capitalize()} - {self.file.name}"
    

class Prompt(models.Model):
    user_prompt = models.TextField()  # The text of the user's prompt
    bot_response = models.TextField(null=True, blank=True)  # The bot's response to the prompt
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the prompt was created

    def __str__(self):
        return f"Prompt: {self.user_prompt[:50]} - Response: {self.bot_response[:50]}"

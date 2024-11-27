from django.db import models

# Create your models here.  
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
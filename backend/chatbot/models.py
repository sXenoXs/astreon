from django.db import models

class Upload(models.Model):
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.TimeField(auto_now=True)
# Create your models here.

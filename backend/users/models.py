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
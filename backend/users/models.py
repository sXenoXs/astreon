from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.timezone import now

class RoleType(models.TextChoices):
    ADMIN = 'admin'
    STUDENT = 'student'
    TEACHER = 'teacher'

class Role(models.Model):
    roleName = models.CharField(max_length=50,choices=RoleType.choices, default=RoleType.STUDENT)
    description = models.TextField()

    def __str__(self):
        return self.roleName

class TimeLog(models.Model):
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(auto_now=True)

class User(AbstractUser):
    timeLog = models.ForeignKey(TimeLog,null=True,blank=True, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE,null=True, blank=True)

class User(AbstractUser):
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=now)   






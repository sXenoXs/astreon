from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.models import EmailAddress
from users.models import CustomUser  # Your custom user model

@receiver(post_save, sender=EmailAddress)
def update_user_verified_status(sender, instance, created, **kwargs):
    if instance.verified:
        try:
            user = CustomUser.objects.get(email=instance.email)
            user.is_verified = True  # Update the user verification status
            user.save()
        except CustomUser.DoesNotExist:
            pass  # Handle case where user does not exist
        
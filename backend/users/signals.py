from allauth.account.signals import email_confirmed
from django.dispatch import receiver
from allauth.account.models import EmailAddress
from users.models import CustomUser  # Your custom user model

@receiver(email_confirmed)
def update_user_verified_status(request, email_address, **kwargs):
    new_email_address =CustomUser.objects.get(email=email_address.email)
    user = CustomUser.objects.get(new_email_address.user)
    user.is_active = True
    user.save()
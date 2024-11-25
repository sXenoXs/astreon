# user_cleanup/management/commands/delete_unverified_users.py
from django.core.management.base import BaseCommand
from django.utils.timezone import now
from users.models import CustomUser  # Ensure this points to the correct model
from allauth.account.models import EmailAddress

class Command(BaseCommand):
    help = 'Delete unverified users after their verification expires'

    def handle(self, *args, **kwargs):
        # Find all unverified users whose verification has expired
        expired_users = CustomUser.objects.filter(
            is_verified=False,
            verification_expiration_date__lte=now()
        )
        deleted_count = 0

        for user in expired_users:
            # Delete associated email addresses
            EmailAddress.objects.filter(user=user).delete()
            # Delete the user
            user.delete()
            deleted_count += 1

        self.stdout.write(self.style.SUCCESS(f'Deleted {deleted_count} expired unverified users.'))

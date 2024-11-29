from django.core.management.base import BaseCommand
from django.utils.timezone import now, timedelta
from django.contrib.auth.models import User
from email_confirmation.models import EmailConfirmation

class Command(BaseCommand):
    help = "Deletes unverified accounts older than 1 week"

    def handle(self, *args, **kwargs):
        # Calculate the expiration threshold
        expiration_threshold = now() - timedelta(weeks=1)

        # Get unverified accounts
        unverified_accounts = EmailConfirmation.objects.filter(confirmed=False, expiration_date__lte=expiration_threshold)

        for confirmation in unverified_accounts:
            user = confirmation.user
            self.stdout.write(f"Deleting unverified account: {user.username}")
            user.delete()

        self.stdout.write("Cleanup completed.")

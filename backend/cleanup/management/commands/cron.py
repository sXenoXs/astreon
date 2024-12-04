from django_cron import CronJobBase, Schedule
from django.utils.timezone import now
from users.models import CustomUser  # Replace with your user model
from allauth.account.models import EmailAddress

class DeleteExpiredUnverifiedUsersJob(CronJobBase):
    RUN_EVERY_MINS = 1440  # Every day

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cleanup.delete_expired_unverified_users'

    def do(self):
        expired_users = CustomUser.objects.filter(
            is_verified=False,
            verification_expiration_date__lte=now()
        )
        for user in expired_users:
            EmailAddress.objects.filter(user=user).delete()
            user.delete()

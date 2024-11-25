from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import send_email_confirmation
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.shortcuts import resolve_url

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user.email = data.get('email')
        user.username = data.get('username')
        if 'password1' in data:
            user.set_password(data["password1"])
        if commit:
            user.save()
            send_email_confirmation(request, user)
        return user
    def get_email_verification_redirect_url(self, email_address):
        # Redirect to the verification complete page
        return resolve_url('/verification-complete/')

class CustomAccountAdapter(DefaultAccountAdapter):
    def respond_user_inactive(self, request, user):
        return HttpResponseRedirect(reverse("account_inactive"))
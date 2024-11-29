from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import send_email_confirmation

class MyAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        data = form.cleaned_data
        #Override the behavior of saving the user automatically
        if not user:
            raise ValueError("User object is none")

        user.username = data['username']
        user.email = data['email']
        if 'password1' in data:
            user.set_password(data['password1'])
        else:
            user.set_unusable_password()
        user.is_active= False
        user.save() #temporary saves user for sending email verificaton
        return user
        send_email_confirmation(request,user)
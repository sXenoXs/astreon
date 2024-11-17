from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.prevent_enumeration = False

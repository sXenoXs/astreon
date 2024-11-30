from allauth.account.forms import SignupForm
from .models import UploadedImage
from .models import UploadedDocument
from django import forms

class CustomSignupForm(SignupForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.prevent_enumeration = False

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']

class DocumentUploadForm(forms.ModelForm):
    prompt = forms.CharField(
        required=False,  # Optional prompt field
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter your prompt...',
            'rows': 4,
            'cols': 50,
        }),
        label="Enter your prompt"
    )

    class Meta:
        model = UploadedDocument
        fields = ['document', 'prompt']  # Include both document and prompt

from django import forms

class SingleFileUploadForm(forms.Form):
    prompt = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter your prompt...',
            'rows': 4,
            'cols': 50,
        })
    )
    file = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'accept': 'application/pdf, text/plain, image/*'})
    )
# forms.py
from django import forms
from .models import UploadedImage
from .models import UploadedDocument

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']

class DocumentUploadForm(forms.ModelForm):
    prompt = forms.CharField(widget=forms.Textarea, label="Enter your prompt")
    
    class Meta:
        model = UploadedDocument
        fields = ['document', 'prompt']  # Include document and prompt in the form

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedDocument
        fields = ['document']

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
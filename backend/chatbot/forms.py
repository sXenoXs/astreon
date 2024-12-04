from django import forms

class UploadForm(forms.Form):
    files = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'allow_multiple_selected': True}),
        required=False,  # Make files optional for general chat
    )
    question = forms.CharField(
        max_length=500,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your request or prompt...'}),
        required=True,
    )



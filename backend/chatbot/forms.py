from django import forms
from .models import Upload
import filetype


class UploadFileForm(forms.Form):
    file = forms.FileField()

    def cleaned_data(self):
        """"
        Validates the file extension uploaded by the user
        returns the uploaded file
        """
        uploaded_file = self.cleaned_data['file']
        allowed_extensions = ['pdf','docx', 'jpg', 'jpeg', 'png']
        file_extension= filetype.guess(uploaded_file)
    

        if file_extension not in allowed_extensions:
            raise forms.ValidationError("Unsupported file type. Please try again ")
        return uploaded_file 

    



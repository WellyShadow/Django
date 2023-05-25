from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArtilesForm(ModelForm):
    class Meta:
        model=Artiles
        fields=['title','announcement','full_text','date']

        widgets = {
            "title":TextInput(attrs={
                'class':'form-control',
                'placeholder':'Name'
            }),
            "announcement":TextInput(attrs={
                'class':'form-control',
                'placeholder':'Announcement'
            }),
            "date":DateTimeInput(attrs={
                'class':'form-control',
                'placeholder':'Date'
            }),
            "full_text":Textarea(attrs={
                'class':'form-control',
                'placeholder':'Text'
            })
        }
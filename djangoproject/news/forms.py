from .models import Artiles
from django.forms import ModelForm


class ArtilesForm(ModelForm):
    class Meta:
        model=Artiles
        fields=['title','announcement','full_text','date']
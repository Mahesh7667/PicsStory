from django import forms
from .models import ImgModel

class ImgForm(forms.ModelForm):
    class Meta:
        model = ImgModel
        fields = ('img','msg',)
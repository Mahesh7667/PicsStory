from django import forms
from .models import ImgModel

class ImgForm(forms.ModelForm):
    class Meta:
        model = ImgModel
        fields = ('img','msg',)
        widgets = {
            'msg': forms.Textarea(attrs={'rows': 8, 'cols': 35}),
        }
from django import forms
from .models import Url_Address

class Url_Form(forms.ModelForm):
    class Meta:
        model = Url_Address
        fields = ('URL',)

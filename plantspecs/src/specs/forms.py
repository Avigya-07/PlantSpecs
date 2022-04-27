import datetime
from django import forms
from django.core.exceptions import ValidationError
from .models import plantUpload
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class plantForm(forms.ModelForm):
    class Meta:
        model=plantUpload
        fields='__all__'    
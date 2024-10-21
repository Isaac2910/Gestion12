from django.core import validators
from django import forms
from .models import User

class studentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'tel' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}), 
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
        }
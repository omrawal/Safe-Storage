from django import forms
from django.forms import fields
from .models import *


class RegistrationForm(forms.ModelForm):
    four_digit_pass = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User_data
        fields = ['username', 'email', 'four_digit_pass',
                  'profile_pic', 'private_key']

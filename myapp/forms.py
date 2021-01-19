from django import forms
from django.forms import ModelForm,Select,ChoiceField

from .models import user


class DateInput(forms.DateInput):
    input_type = 'date'

gender_choices = [('male', 'Male'), ('female','Female'),('others','Others')]

class Register(ModelForm):

    class Meta:
        model = user
        fields = ['name', 'mail', 'addr', 'phone', 'dob', 'gender']
        widgets = {
            'dob': DateInput(),
            'gender': Select(choices=gender_choices)
        }

class loginForm(forms.Form):
	username = forms.CharField(max_length = 100)
	password = forms.CharField(widget = forms.PasswordInput())
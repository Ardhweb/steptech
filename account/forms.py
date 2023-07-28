from django.forms import ModelForm
from django import forms
from .models import User

class UserForm(ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('name','email', 'role')
        widgets = {
            'name':forms.TextInput(attrs={"class": "form-control", "placeholder":"Your Name e.g 'Akash' "}),
            'email':forms.EmailInput(attrs={"class": "form-control", "placeholder":"Add Your Email Address here @"}),
            'role':forms.Select(attrs={"class": "form-control"}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

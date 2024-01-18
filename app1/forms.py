from django import forms
from .models import user
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User






class Signupform(UserCreationForm):
    first_name = forms.CharField(max_length=30,label='First Name:')
    last_name = forms.CharField(max_length=30,)
    email = forms.EmailField(max_length=30,)
    password1=forms.CharField(label="Password",)
    password2=forms.CharField(label="Re-enter Password",)
    username = forms.CharField(
                    max_length=100,
                    widget=forms.TextInput(attrs={'class': 'FOO_CLASS'}))    
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'username','email' ]

class MyChangePasswordForm(PasswordChangeForm):
     old_password=forms.CharField(label="old password"),
     strip=False,
     widget=forms.PasswordInput(attrs={'class':'form-control'})

     new_password1=forms.CharField(label="New Password 1"),
     strip=False,
     widget=forms.PasswordInput(attrs={'class':'form-control'})     

     new_password2=forms.CharField(label="Confirm Password"),
     strip=False,
     widget=forms.PasswordInput(attrs={'class':'form-control'}) 


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)
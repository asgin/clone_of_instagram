from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import InstaUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True, help_text='это поле обязательно для заполнения')
    bio = forms.CharField(max_length=255, required=False)
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    class Meta:
        model = InstaUser
        fields = ['username', 'email', 'bio', 'first_name', 'last_name', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(max_length=255, required=True)
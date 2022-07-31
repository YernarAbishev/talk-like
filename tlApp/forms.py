from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label="First name", max_length=101)
    last_name = forms.CharField(label="Last name", max_length=101)
    email = forms.EmailField(label="E-mail")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'bio')

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)


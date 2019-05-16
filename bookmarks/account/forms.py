from django import forms

from django.contrib.auth.models import User

from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_two = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

    def clean_password_two(self, *args, **kwargs):
        cleaned_data = self.cleaned_data
        if cleaned_data['password'] != cleaned_data['password_two']:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data['password_two']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    success_url = reverse_lazy('login')
    template_name="users/signup.html"
    form_class=CustomUserCreationForm

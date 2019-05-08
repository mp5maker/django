from django.shortcuts import render

from django.views.generic.edit import CreateView

from django.urls import reverse_lazy

from .models import CustomUser

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    template_name = "accounts/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
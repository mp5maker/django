from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

from django.contrib.auth import views as auth_views

from django.contrib.auth.mixins import LoginRequiredMixin

class SignUpView(CreateView):
    template_name="users/signup.html"
    form_class=CustomUserCreationForm
    success_url = reverse_lazy('login')

class PasswordChangeView(LoginRequiredMixin, auth_views.PasswordChangeView):
    redirect_url = reverse_lazy('users:login')


class PasswordChangeDoneView(LoginRequiredMixin, auth_views.PasswordChangeDoneView):
    redirect_url = reverse_lazy('users:login')

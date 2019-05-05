from django.shortcuts import render

from django.views.generic import ListView

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post


class PostHomeViewPage(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/home.html'
    login_url = reverse_lazy("login")

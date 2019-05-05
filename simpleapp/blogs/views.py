from django.shortcuts import render

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post

class BlogListPageView(LoginRequiredMixin, ListView):
    template_name = "blogs/home.html"
    model = Post
    login_url=reverse_lazy('login')


class BlogDetailPageView(LoginRequiredMixin, DetailView):
    template_name = "blogs/details.html"
    model = Post
    login_url = reverse_lazy('login')


class BlogCreatePageView(LoginRequiredMixin, CreateView):
    template_name="blogs/create.html"
    model=Post
    fields=('title', 'author', 'body')
    login_url = reverse_lazy('login')


class BlogUpdatePageView(LoginRequiredMixin, UpdateView):
    template_name="blogs/update.html"
    model=Post
    fields=('title', 'body', 'author')
    login_url = reverse_lazy('login')


class BlogDeletePageView(LoginRequiredMixin, DeleteView):
    template_name="blogs/delete.html"
    model=Post
    success_url=reverse_lazy('blogs:list')
    login_url = reverse_lazy('login')

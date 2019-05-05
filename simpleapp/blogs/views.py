from django.shortcuts import render

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Post

class BlogListPageView(ListView):
    template_name = "blogs/home.html"
    model = Post

class BlogDetailPageView(DetailView):
    template_name = "blogs/details.html"
    model = Post

class BlogCreatePageView(CreateView):
    template_name="blogs/create.html"
    model=Post
    fields=('title', 'author', 'body')

class BlogUpdatePageView(UpdateView):
    template_name="blogs/update.html"
    model=Post
    fields=('title', 'body', 'author')

class BlogDeletePageView(DeleteView):
    template_name="blogs/delete.html"
    model=Post
    success_url=reverse_lazy('blogs:list')
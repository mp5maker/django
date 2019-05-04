from django.shortcuts import render

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView

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
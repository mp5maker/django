from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Post

class BlogListPageView(ListView):
    template_name = "blogs/home.html"
    model = Post

class BlogDetailPageView(DetailView):
    template_name = "blogs/details.html"
    model = Post
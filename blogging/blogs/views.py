from django.shortcuts import render, get_object_or_404

from .models import Post

def post_list_view(request, *args, **kwargs):
    posts = Post.objects.all()
    return render(request, 'blogs/posts/list.html', {"posts": posts})

def post_details_view(request, *args, **kwargs):
    slug = kwargs.get('slug')
    post = get_object_or_404(Post, slug=slug, status='published')
    return render(request, 'blogs/posts/details.html', {"post": post})
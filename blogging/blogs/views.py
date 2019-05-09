from django.shortcuts import render, get_object_or_404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.conf import settings

from .models import Post

def post_list_view(request, *args, **kwargs):
    posts = Post.objects.all().filter(status="published")
    paginator = Paginator(posts, settings.PAGINATION_SIZE)
    requested_page_number = request.GET.get('page')
    try:
        posts = paginator.get_page(requested_page_number)
    except PageNotAnInteger:
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(paginator.num_pages)
    return render(request, 'blogs/posts/list.html', { "posts": posts })

def post_details_view(request, *args, **kwargs):
    slug = kwargs.get('slug')
    year = kwargs.get('year')
    month = kwargs.get('month')
    day = kwargs.get('day')
    post = get_object_or_404(Post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=slug,
        status='published')
    return render(request, 'blogs/posts/details.html', {"post": post})

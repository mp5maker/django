from django.shortcuts import render, get_object_or_404

from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView

from django.views.generic.edit import UpdateView, CreateView, DeleteView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.conf import settings

from django.core.mail import send_mail

from django.db.models import Count

from taggit.models import Tag

from .models import Post

from .forms import (
    EmailPostForm,
    CommentForm
)

def post_list_view(request, *args, **kwargs):
    posts = Post.published.all()

    tag_slug = kwargs.get('slug')
    tag = None
    if tag_slug:
        tag_slug = kwargs.get('slug').split("-")
        tag = list(Tag.objects.values('id').filter(slug__in=tag_slug))
        posts = posts.filter(tags__in=[t['id'] for t in tag]).distinct()

    paginator = Paginator(posts, settings.PAGINATION_SIZE)
    requested_page_number = request.GET.get('page')
    try:
        posts = paginator.get_page(requested_page_number)
    except PageNotAnInteger:
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(paginator.num_pages)

    return render(request, 'blogs/posts/list.html', {
        "posts": posts,
        "tag": tag
    })

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

    comments = post.comments.filter(active=True)
    comments_paginator = Paginator(comments, 2)
    requested_page_number = request.GET.get('page')
    try:
        comments = comments_paginator.get_page(requested_page_number)
    except PageNotAnInteger:
        comments = comments_paginator.get_page(1)
    except EmptyPage:
        comments = comments_paginator.get_page(comments_paginator.num_pages)

    new_comment = None
    if (request.method == 'POST'):
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)
    similar_posts = similar_posts.annotate(
        same_tags=Count('tags')
    ).order_by(
        '-same_tags',
        '-publish'
    )[:4]

    return render(request, 'blogs/posts/details.html', {
        "post": post,
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form,
        "similar_posts": similar_posts
    })

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = settings.PAGINATION_SIZE
    template_name = 'blogs/posts/list.html'

    def get_queryset(self):
        return Post.objects.filter(status="published")

class PostCreateView(CreateView):
    template_name = 'blogs/posts/create.html'
    model = Post
    fields = ('title', 'body', 'author', 'status',)

class PostUpdateView(UpdateView):
    template_name = 'blogs/posts/update.html'
    model = Post
    fields = ('title', 'body', 'author', 'status',)

class PostDeleteView(DeleteView):
    template_name = 'blogs/posts/delete.html'
    model = Post
    success_url = reverse_lazy('blogs:posts-list')

def post_share(request, *args, **kwargs):
    post_id = kwargs.get('post_id')
    post = get_object_or_404(Post, id=post_id, status="published")
    sent = False

    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cleaned_form_data = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = "{} ({}) recommends you reading {}".format(
                cleaned_form_data['name'],
                cleaned_form_data['email'],
                post.title,
            )
            message = "Read '{}' at {} \n\n {}\s comments: {}".format(
                post.title,
                post_url,
                cleaned_form_data['name'],
                cleaned_form_data['comments'],
            )
            send_mail(subject, message, 'admin@test.com', [
                cleaned_form_data['to']
            ])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blogs/email/share.html', {
        "post": post,
        "form": form,
        "sent": sent
    })

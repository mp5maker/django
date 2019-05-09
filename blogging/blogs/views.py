from django.shortcuts import render, get_object_or_404

from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView

from django.views.generic.edit import UpdateView, CreateView, DeleteView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.conf import settings

from django.core.mail import send_mail

from .models import Post

from .forms import EmailPostForm


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

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = settings.PAGINATION_SIZE
    template_name = 'blogs/posts/list.html'

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

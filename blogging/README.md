## Shell Plus ##

    from accounts.models import CustomUser
    from blogs.models import Post

### List ###

    all_posts = Post.objects.all()

### Filter ###

    filtered_post = Post.objects.filter(publish__year=2019)
    filtered_post = Post.objects.filter(author__username='user')
    filtered_chain_post = Post.objects.filter(publish__year=2019).filter(author__username='user')
    filter_data = Post.objects.filter(author__username='user') # Damn, Wage
    filter_data.exclude(title__startswith='Damn') # Wage
    filter_data.filter(title__startswith='Damn') # Damn

### Ordering ###

    order_by = Post.objects.order_by('title') # Descending Order
    order_by = Post.objects.order_by('-title') # Ascending Order

### Slicing ###

    print(Post.objects.all()[:3])

### Create ###

    user = CustomUser.objects.filter(id=1) # Gives the queryset
    user = CustomUser.objects.get(id=1) # Gives the instance
    post = Post(title="Damn", body="Shocking", author=user, slug="shocking") # Prepare Post Object
    post.save() # Create the Post

### Delete ###

    post = Post.objects.get(id=1)
    post.delete()

### blogs.manager ###

    from django.db import models

    class PublishedManager(models.Manager):
        return super(PublishedManager, self).get_queryset().filter(status='draft')

### templates.blogs.posts.list.html ###

    <p>{{ post.body|truncatewords:30|linebreaks }}</p>

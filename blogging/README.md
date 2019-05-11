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

### Pg Admin ###

    sudo apt-get install libpq-dev python-dev
    sudo apt-get install postgresql postgresql-contrib

    sudo passwd postgres
    sudo -u postgres psql
    ALTER USER postgres PASSWORD 'postgres';
    locate pg_hba.conf
    copy /etc/postgresql/10/main/pg_hba.conf
    sudo nano /etc/postgresql/10/main/pg_hba.conf

    local | all | postgres | peer
    ----- |---- |--------- |-----
    local | all | postgres | trust

    sudo service postgresql restart

    su postgres

    psql
    CREATE USER sample_user WITH PASSWORD 'sample_password';
    CREATE DATABASE sample_database WITH OWNER sample_user;
    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO sample_user;
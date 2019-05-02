# Django #

    pip install django-admin
    pip install virtualenvwrapper
    pip install autopep8
    pip install pyling
    pip install pipenv
    mkvirtualenv django-tutorial
    workon django-tutorial
    django-admin startapp simpleapp

    cd simpleapp
    python manage.py migrate

    user: user
    email: user@gmail.com
    password: test1234

    python manage.py runserver
    python manage.py startapp pages

    os.path.join(BASE_DIR, 'templates')

### page.views ###

    from django.shortcuts import render
    from django.http import HttpResponse
    from django.views.generic import TemplateView


### page.urls ###

    from django.urls import path

### pages.test ###

    from django.test import SimpleTestCase
    python manage.py test

### config.urls ###

    from django.urls import include

### config.settings ###

    import django_heroku
    INSTALLED_APPS = [ ..., 'pages' ]
    TEMPLATES = [
        {
            'DIRS': [ os.path.join(BASE_DIR, 'templates') ],
            ...
        },
    ]
    MIDDLEWARE_CLASSES = (
        'whitenoise.middleware.WhiteNoiseMiddleware',
        ...
    )
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]
    STATIC_URL = '/static/'
    django_heroku.settings(locals())

### Root ###

    touch Procfile
    pipenv install gunicorn
    pip install whitenoise
    pip install django-heroku
    cd config
    mkdir static
    cd static
    touch .keep
    pip freeze > requirements.txt
    rm Pipfile
    pipenv lock

### Procfile ###

    web: gunicorn config.wsgi --log-file -

### posts.model ###

    import django.models import models
    python manage.py makemigrations
    python manage.py migrate

    from django.db import models
    from django.utils import timezone
    from django.template.defaultfilters import slugify

    class Post(models.Model):
        text = models.TextField()
        slug = models.SlugField(blank=True)
        created_at = models.DateTimeField(editable=False, default=timezone.now)
        updated_at = models.DateTimeField()

        def __str__(self):
            """ A string representation of the model """
            return self.text[:50]

        def save(self, *args, **kwargs):
            self.slug = slugify(self.text)
            if not self.id:
                self.created_at = timezone.now()
            self.updated_at = timezone.now()
            return super(Post, self).save(*args, **kwargs)


### posts.admin ###

    import django.contrib import admin
    from .models import Post
    admin.site.register(Post)

### template.posts.home.html ###

    {% extends 'base.html' %}
    {% block content %}
        <div class="container-fluid">
            <div class="row">
                <div class="col p-5 m-5 box-shadow">
                    <h1>Posts</h1>
                    {% for post in object_list %}
                        <div class="card mb-3">
                            <div class="card-body">
                                <p class="card-text">
                                    {{ post.text }}
                                </p>
                            </div>
                            <div class="card-footer">
                                Published On: {{ post.created_at }}
                            </div>
                        </div>
                    {% endfor %}
                </div>
            </div>
        </div>
    {% endblock %}

### posts.views ###

    class PostHomeViewPage(TemplateView):
        model = Post
        template_name = 'posts/home.html'
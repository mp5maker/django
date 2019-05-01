# Django #

    pip install django-admin
    pip install autopep8
    pip install pyling
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


### config.urls ###

    from django.urls import include

### config.settings ###

    INSTALLED_APPS = [ ..., 'pages' ]
    TEMPLATES = [
        {
            'DIRS': [ os.path.join(BASE_DIR, 'templates') ],
            ...
        },
    ]
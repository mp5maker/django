# Newspaper #

### config.settings ###
    INSTALLED_APPS = [
        'crispy_forms',
        ...
    ]

    AUTH_USER_MODEL = 'users.CustomUser'
    CRISPY_TEMPLATE_PACK = 'bootstrap4'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    EMAIL_HOST = 'smtp.sendgrid.com'
    EMAIL_HOST_USER = 'mp5maker'
    EMAIL_HOST_PASSWORD = 'boom'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True

### users.model ###

    import django.contrib.auth.models import AbstractUser
    class CustomUser(AbstractUser):
        age=models.PositiveIntegerField(default=0)

### users.forms ###

    import django.contrib.auth.forms import UserCreationForm, UserChangeForm
    from .models import CustomUser

    class CustomUserCreationForm(AbstractUser):
        class Meta(UserCreationForm.Meta):
             model=CustomUser
             field=UsrCreationForm.Mete.fields

### users.admin ###
        from django.contrib import admin
        from django.contrib.auth.admin import UserAdmin
        from .forms import CustomUserChangeForm, CustomUserCreationForm
        from .models import CustomUser


        class CustomUserAdmin(UserAdmin):
        add_form = CustomUserCreationForm
        form = CustomUserChangeForm
        list_display = ['email', 'username', 'age']
        model = CustomUser
        admin.site.register(CustomUser, CustomUserAdmin)

        python manage.py makemigrations
        python manage.py migrate

## Crispy Forms ###

        pipenv install django-crispy-forms

## templates.registration.login
        {% extends 'base.html' %}
        {% block title %}
        <div>
                <h4>
                Login
                </h4>
        </div>
        {% endblock %}
        {% block content %}
        <div class="box-shadow">
                <form method="POST" action="">
                {% csrf_token %}
                {{ form|crispy }}
                <p>
                    <input type="submit" class="btn btn-primary" value="Submit"/>
                </p>
                </form>
        </div>
        {% endblock %}
# Newspaper #

### config.settings ###

    AUTH_USER_MODEL = 'users.CustomUser'

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
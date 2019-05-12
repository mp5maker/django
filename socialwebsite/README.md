### Social Websites ###


#### Installation ####

    pip install social-auth-app-django

#### config.settings.py ####

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Third Party Apps
        'django_heroku',
        'crispy_forms',
        'whitenoise.runserver_nostatic',
        'django_extensions',
        'social_django',

        # App
        'account'
    ]

    AUTHENTICATION_BACKENDS = [
        'django.contrib.auth.backends.ModelBackend',
        'account.authentication.EmailAuthBackend',
        'social_core.backends.facebook.FacebookOAuth2',
        'social_core.backends.twitter.TwitterOAuth'
        'social_core.backends.google.GoogleOAuth2'
    ]

    SOCIAL_AUTH_FACEBOOK_KEY = '******'
    SOCIAL_AUTH_FACEBOOK_SECRET = '****'
    SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

    SOCIAL_AUTH_TWITTER_KEY = '*****'
    SOCIAL_AUTH_TWITTER_SECRET = '****'


#### config.urls.py ####

    from django.contrib import admin
    from django.urls import path, include
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('accounts/', include('account.urls', namespace="accounts")),
        path('social-auth/', include('social_django.urls', namespace="social")),
    ]

    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#### Websites For Socials ####

    https://developers.facebook.com/apps/
    https://apps.twitter.com/app/new
    https://console.developers.google.com/apis/credentials


#### Valid OAuth Redirection URL ####

    https://localhost:8000/social-auth/complete/facebook/
from django.urls import path

from .views import (testPageView, HomePageView, AboutPageView)

app_name = "pages"

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('test/', testPageView, name="test")
]
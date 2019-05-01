from django.urls import path

from .views import (testPageView, HomePageView, AboutPageView)

app_name = "pages"

urlpatterns = [
    path('test/', testPageView, name="test"),
    path('home/', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about")
]
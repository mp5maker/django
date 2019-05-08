from django.urls import path

from .views import post_list_view, post_details_view

app_name = "blogs"

urlpatterns = [
    path('posts/', post_list_view, name="posts-list"),
    path('posts/<slug:slug>', post_details_view, name="posts-details"),
]
from django.urls import path

from .views import (
    BlogListPageView,
    BlogDetailPageView,
    BlogCreatePageView,
    BlogUpdatePageView
)

app_name = "blogs"

urlpatterns = [
    path('',  BlogListPageView.as_view(), name="list"),
    path('create/',  BlogCreatePageView.as_view(), name="create"),
    path('edit/<slug:slug>/',  BlogUpdatePageView.as_view(), name="update"),
    path('<slug:slug>/',  BlogDetailPageView.as_view(), name="details")
]

from django.urls import path

from .views import BlogListPageView, BlogDetailPageView, BlogCreatePageView

app_name = "blogs"

urlpatterns = [
    path('',  BlogListPageView.as_view(), name="list"),
    path('create/',  BlogCreatePageView.as_view(), name="create"),
    path('<slug:slug>/',  BlogDetailPageView.as_view(), name="details")
]

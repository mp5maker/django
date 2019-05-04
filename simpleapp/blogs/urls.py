from django.urls import path

from .views import BlogListPageView, BlogDetailPageView

app_name = "blogs"

urlpatterns = [
    path('',  BlogListPageView.as_view(), name="list"),
    path('<slug:slug>/',  BlogDetailPageView.as_view(), name="details")
]

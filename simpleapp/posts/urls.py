from django.urls import path

from .views import PostHomeViewPage

app_name = "posts"

urlpatterns = [
    path('', PostHomeViewPage.as_view(), name="home")
]

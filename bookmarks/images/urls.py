from django.urls import path

from .views import (
    image_create,
    image_details,
    image_like
)

app_name = "images"

urlpatterns = [
    path('create/', image_create, name="create"),
    path('details/<int:id>/<slug:slug>/', image_details, name="details"),
    path('like/', image_like, name="like"),
]
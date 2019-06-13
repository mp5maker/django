from django.urls import path

from .views import (
    DescriptionListCreateView
)

app_name = "images"

urlpatterns = [
    path('description/', DescriptionListCreateView.as_view(), name="description-list-create")
]
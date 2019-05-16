from django.urls import path

from .views import dashboard

app_name = "pages"

urlpatterns = [
    path('', dashboard, name="dashboard")
]
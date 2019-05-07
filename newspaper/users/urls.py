from django.urls import path

from .views import (
    SignUpView,
    PasswordChangeView,
    PasswordChangeDoneView
)

from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('password-change/', PasswordChangeView.as_view(), name="password_change"),
    path('password-change/done', PasswordChangeDoneView.as_view(), name="password_change_done")
]

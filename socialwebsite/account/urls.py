from django.urls import path, re_path

from .views import (
    user_login,
    dashboard,
    register,
    edit
)

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

app_name = "accounts"

urlpatterns = [
    # path('login/', user_login, name="login"),
    # path('', include('django.contrib.auth.urls')) # root
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('password-change/', PasswordChangeView.as_view(
        template_name="registration/password-change.html",
        success_url="/  accounts/password-change/done/"
    ),
        name="password-change"
    ),
    path('password-change/done/', PasswordChangeDoneView.as_view(
        template_name="registration/password-change-done.html"
    ),
        name="password-change-done"
    ),
    path('password/reset/', PasswordResetView.as_view(
        template_name="registration/password-reset.html",
        email_template_name="registration/password-reset-email.html",
        success_url="/accounts/password/reset/done/",
        from_email="admin@socialnetwork.com"
    ),
        name="password-reset"
    ),
    path('password/reset/done/', PasswordResetDoneView.as_view(
        template_name="registration/password-reset-done.html"
    ),
        name="password-reset-done"
    ),
    re_path('password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', PasswordResetConfirmView.as_view(
        template_name="registration/password-reset-confirm.html",
        success_url='/accounts/password/reset/complete/'
    ),
        name="password-reset-confirm"
    ),
    path('password/reset/complete/', PasswordResetCompleteView.as_view(
        template_name="registration/password-reset-complete.html"
    ),
        name="password-reset-complete"
    ),
    path('registration/', register, name="signup"),
    path('edit/', edit, name="edit"),
    path('dashboard/', dashboard, name="dashboard"),
]
from django.urls import path

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from django.urls import reverse_lazy

from .views import (
    user_login,
    register,
    edit
)

app_name = 'account'

urlpatterns = [
    # path('login/', user_login, name='login'),
    path('signup/', register, name='signup'),
    path('login/', LoginView.as_view(
        template_name="account/login.html",
    ), name='login'),
    path('logout/', LogoutView.as_view(
        next_page=reverse_lazy("account:login")
    ), name='logout'),
    path('password-change/', PasswordChangeView.as_view(
        template_name="account/password-change.html",
        success_url=reverse_lazy("account:password-change-done")
    ), name="password-change"),
    path('password-change/done/', PasswordChangeDoneView.as_view(
        template_name="account/password-change-done.html",
    ), name="password-change-done"),
    path('password-reset/', PasswordResetView.as_view(
        template_name="account/password-reset.html",
        email_template_name="account/password-reset-email.html",
        subject_template_name="account/password-reset-subject.txt",
        success_url=reverse_lazy("account:password-reset-done")
    ), name="password-reset"),
    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name="account/password-reset-done.html",
    ), name="password-reset-done"),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name="account/password-reset-confirm.html",
        success_url=reverse_lazy('account:password-reset-complete')
    ), name="password-reset-confirm"),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(
        template_name="account/password-reset-complete.html",
    ), name="password-reset-complete"),
    path('profile/edit/', edit, name="profile-edit"),
]

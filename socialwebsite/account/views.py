from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy

from .forms import (
    LoginForm,
    RegistrationForm,
    UserEditForm,
    ProfileEditForm
)

from .models import Profile

def user_login(request, *args, **kwargs):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(
                request,
                username=cleaned_data['user'],
                password=cleaned_data['pasword']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated Successfully')
            else:
                return HttpResponse('Disabled Account')
        else:
            return HttpResponse('Invalid Account')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {"form": form})


@login_required(login_url=reverse_lazy('accounts:login'))
def dashboard(request, *args, **kwargs):
    return render(request, 'accounts/dashboard.html', {"section": 'dashboard'})


def register(request, *args, **kwargs):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form['password']
            )
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'accounts/register-done.html', {
                "new_user": new_user
            })
    else:
        user_form = RegistrationForm()
        return render(request, 'accounts/register.html', { "form": user_form })

@login_required(login_url=reverse_lazy('accounts:login'))
def edit(request, *args, **kwargs):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(
        request,
        'accounts/edit.html',
        {
            "user_form": user_form,
            "profile_form": profile_form
        }
    )
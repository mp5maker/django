from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.urls import reverse_lazy

from .forms import (
    LoginForm,
    UserRegistrationForm,
    UserEditForm,
    ProfileEditForm
)

def user_login(request):
    if request.method == 'POST':
        form =  LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(
                username=cleaned_data['username'],
                password=cleaned_data['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    HttpResponse('Authenticated Successfully')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', { "form": form })


def register(request, *args, **kwargs):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data['password']
            )
            new_user.save()
            return render(request, 'account/signup-done.html', {"new_user": new_user})
    else:
        form = UserRegistrationForm()
    return render(request, 'account/signup.html', { "form": form })

@login_required(login_url=reverse_lazy('account:login'))
def edit(request, *args, **kwargs):
    if request.method == "POST":
        user_edit_form = UserEditForm(
            instance=request.user,
            data=request.POST
        )
        profile_edit_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        if user_edit_form.is_valid() and profile_edit_form.is_valid():
            user_edit_form.save()
            profile_edit_form.save()
            messages.success(request, "Profile Updated Successfully")
        else:
            messages.error(request, "Error updating your profile")
    else:
        user_edit_form = UserEditForm(instance=request.user)
        profile_edit_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/profile-edit.html', {
        "forms" : [user_edit_form, profile_edit_form]
    })

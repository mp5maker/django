from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth import authenticate, login

from .forms import LoginForm


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
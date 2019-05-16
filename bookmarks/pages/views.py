from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy

@login_required(login_url=reverse_lazy('account:login'))
def dashboard(request, *args, **kwargs):
    return render(request, 'pages/dashboard.html', {"section": "dashboard"})
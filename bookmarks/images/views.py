from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import ImageCreateForm

@login_required(login_url="account:login")
def image_create(request):
    if request.method == "POST":
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Images Added Successfully')
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)

    return render(request, "images/create.html", {"section": "images", "form": form})

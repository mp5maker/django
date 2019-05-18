from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from django.views.decorators.http import require_POST

from django.contrib import messages

from django.http import JsonResponse

from .forms import ImageCreateForm

from .models import Image

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


def image_details(request, *args, **kwargs):
    id = kwargs.get('id')
    slug = kwargs.get('slug')
    image = get_object_or_404(Image, id = id, slug=slug)
    return render(
        request, 'images/details.html', {
            "section": "images",
            "image": image
        }
    )

@login_required(login_url="account:login")
@require_POST
def image_like(request, *args, **kwargs):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': '404'})
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy

from images.models import Image

from actions.models import Action


@login_required(login_url=reverse_lazy('account:login'))
def dashboard(request, *args, **kwargs):
    actions = Action.objects.exclude(user=request.user)
    following_ids = request.user.following.values_list('id', flat=True)

    if following_ids:
        actions = actions.filter(user_id__in=following_ids)
    actions = actions.select_related('user', 'user__profile').prefetch_related('target')[:10]
    images_by_popularity = Image.objects.order_by('-total_likes')
    return render(request, 'pages/dashboard.html', {
        "section": "dashboard",
        "actions": actions,
        "images_by_popularity": images_by_popularity
    })

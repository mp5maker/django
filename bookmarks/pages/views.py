from django.shortcuts import render

from common.utils import redis_cache

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

    # Popular Images
    images_by_popularity = Image.objects.order_by('-total_likes')

    # Most Viewed Images
    redis = redis_cache()
    image_ranking = redis.zrange('image_ranking', 0, -1, desc=True)[:10]
    image_ranking_ids = [int(id) for id in image_ranking]
    most_viewed = list(Image.objects.filter(
        id__in=image_ranking_ids
    ))
    most_viewed.sort(key=lambda image: image_ranking_ids.index(image.id))

    return render(request, 'pages/dashboard.html', {
        "section": "dashboard",
        "actions": actions,
        "images_by_popularity": images_by_popularity,
        "most_viewed": most_viewed
    })

from django.db import models

from articles.models import Article

from django.conf import settings

from django.urls import reverse

class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    comments = models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.comments[:50]

    def get_absolute_url(self):
        return reverse('articles:list')
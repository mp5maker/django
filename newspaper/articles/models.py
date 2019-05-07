from django.db import models

from django.conf import settings

from django.urls import reverse

from django.utils.timezone import now

from django.template.defaultfilters import slugify

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    body = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title[:50]

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = now()
            self.slug = slugify(self.title[:50])
        self.updated_at = now()
        return super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('articles:details', kwargs={"slug": self.slug})
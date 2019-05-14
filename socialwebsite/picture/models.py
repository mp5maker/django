from django.db import models

from django.conf import settings

from django.utils.text import slugify

from django.utils.timezone import now

from django.urls import reverse

class Picture(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="images_created"
    ),
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to="images/%Y/%m/%d")
    description = models.TextField(blank=True)
    created = models.DateTimeField()
    users_like = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="images_liked",
        blank=True
    )

    def __str__(self):
        return self.title[:50]

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title[:50])
            self.created = now()
        return super(Picture, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('accounts:dashboard')

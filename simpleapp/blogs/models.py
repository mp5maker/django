from django.db import models

from django.utils.timezone import now

from django.template.defaultfilters import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    body = models.TextField()
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.title[:50]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if not self.id:
            self.created_at = now()
        self.updated_at = now()
        return super(Post, self).save(*args, **kwargs)
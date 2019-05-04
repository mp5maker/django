from django.db import models

from django.utils.timezone import now

from django.template.defaultfilters import slugify

class Post(models.Model):
    text = models.TextField()
    slug = models.SlugField(blank=True)
    created_at = models.DateTimeField(editable=False, default=now)
    updated_at = models.DateTimeField()

    def __str__(self):
        """ A string representation of the model """
        return self.text[:50]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.text)
        if not self.id:
            self.created_at = now()
        self.updated_at = now()
        return super(Post, self).save(*args, **kwargs)

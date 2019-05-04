from django.db import models

from django.utils.timezone import now

from django.template.defaultfilters import slugify

from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    body = models.TextField()
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.title[:50]

    def save(self, *args, **kwargs):
        slug = slugify(self.title[:25])
        slug_exists = Post.objects.filter(slug=slug).exists()
        if slug_exists:
            self.slug = slug + "-another"
        else:
            self.slug = slug
        if not self.id:
            if not self.created_at:
                self.created_at = now()
        if not self.updated_at:
            self.updated_at = now()
        return super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blogs:details', kwargs={"slug": str(self.slug)})
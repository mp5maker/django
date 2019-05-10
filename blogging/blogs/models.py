from django.db import models

from django.contrib.auth.models import User

from django.conf import settings

from django.utils.timezone import now

from django.template.defaultfilters import slugify

from .enums import STATUS_CHOICES

from django.urls import reverse

from .managers import PublishedManager


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique_for_date='publish', blank=True)
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blog_posts"
    )
    publish = models.DateTimeField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title[:50]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title[:50])
        if not self.id:
            self.publish = now()
            self.created = now()
        self.updated = now()
        return super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blogs:posts-details', kwargs={
            "slug": self.slug,
            "year": self.publish.year,
            "month": self.publish.month,
            "day": self.publish.day
        })

    class Meta:
        ordering = ('-publish',)


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    slug=models.SlugField(blank=True)
    name=models.CharField(max_length=200)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(blank=True)
    updated=models.DateTimeField(blank=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering = ('created', )

    def __str__(self):
        return self.name[:50]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name[:50])
        if not self.id:
            self.created = now()
        self.updated = now()
        return super(Comment, self).save(*args, **kwargs)

    def get_absolute_url(self, *args, **kwargs):
        return reverse("blogs:posts-detail", kwargs = {
            "slug": self.post.slug,
            "year": self.post.publish.year,
            "month": self.post.publish.month,
            "day": self.post.publish.month
        })



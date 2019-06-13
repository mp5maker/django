from django.db import models

from django.utils.timezone import now

from django.utils.text import slugify

class Common(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(blank=True)

    class Meta:
        abstract = True
        ordering = ('created', )

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = now()
            self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        self.updated = now()
        super(Common, self).save(*args, **kwargs)


class Description(Common):
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name[:20]


class Images(Common):
    image = models.ImageField(blank=True, upload_to="images/%y/%m/%d")
    description = models.ForeignKey(
        Description,
        on_delete=models.CASCADE,
        related_name="images"
    )

    def __str__(self):
        return self.name[:20]
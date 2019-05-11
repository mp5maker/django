from django.contrib.sitemaps import Sitemap

from .models import Post

class PostSiteMap(Sitemap):
    changefreq = 'always'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated
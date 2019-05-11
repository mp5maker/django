from django.contrib.syndication.views import Feed

from django.utils.feedgenerator import Atom1Feed

from django.template.defaultfilters import truncatewords

from .models import Post

class LatestPostsFeed(Feed):
    title = 'My Blog'
    link = '/blogs/'
    description = 'New posts of my blog'
    description_template = "blogs/feeds/feeds.html"

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)

    def get_context_data(self, **kwargs):
        return  super().get_context_data(**kwargs)


class AtomSiteNewsFeed(LatestPostsFeed):
    feed_type = Atom1Feed
    subtitle = LatestPostsFeed.description

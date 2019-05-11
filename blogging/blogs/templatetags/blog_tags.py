from django import template

from django.db.models import Count

from django.utils.safestring import mark_safe

from markdownx.utils import markdownify

from ..models import Post

register = template.Library()

@register.simple_tag
def total_posts(name='total_posts'):
    return Post.published.count()

@register.inclusion_tag('blogs/layouts/most_commented_posts.html')
def show_most_commented_posts(count=5):
    commented_posts = Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]
    return {
        "commented_posts": commented_posts
    }

@register.inclusion_tag('blogs/layouts/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts }


@register.filter(name='markdown')
def perform_markdown(value):
    return mark_safe(markdownify(value))
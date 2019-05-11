from django.urls import path, re_path

from .views import (
    post_list_view,
    post_details_view,
    post_share,
    post_search,
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

from .feeds import AtomSiteNewsFeed

app_name = "blogs"

# Post CRUD
urlpatterns = [
    path('posts/', post_list_view, name="posts-list"),
    path('posts/tag/<slug:slug>', post_list_view, name="posts-list-tag"),
    path('posts/<int:year>/<int:month>/<int:day>/<slug:slug>',
        post_details_view,
        name="posts-details"
    ),
    path('posts/create/', PostCreateView.as_view(), name="posts-create"),
    path('posts/update/<int:year>/<int:month>/<int:day>/<slug:slug>',
        PostUpdateView.as_view(),
        name="posts-update"
    ),
    path('posts/delete/<int:year>/<int:month>/<int:day>/<slug:slug>',
        PostDeleteView.as_view(),
        name="posts-delete"
    ),
    path('posts/search/', post_search, name="posts-search")
]

# Email
urlpatterns += [
    path('posts/share/<int:post_id>', post_share, name="posts-email-share")
]

# Feed
urlpatterns += [
    path('feed/', AtomSiteNewsFeed(), name="posts-feed")
]

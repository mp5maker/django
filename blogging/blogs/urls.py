from django.urls import path

from .views import (
    post_list_view,
    post_details_view,
    post_share,
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

app_name = "blogs"

# Post CRUD
urlpatterns = [
    path('posts/', PostListView.as_view(), name="posts-list"),
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
]

# Email
urlpatterns += [
    path('posts/share/<int:post_id>', post_share, name="posts-email-share")
]

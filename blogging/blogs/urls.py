from django.urls import path

from .views import (
    post_list_view,
    post_details_view,
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

app_name = "blogs"

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
    )
]

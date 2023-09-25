from django.urls import path
from .views import (
    PostsCreateView,
    PostsUpdateView,
    PostsDeleteView,
    PostsDetailView,
    PostsListView,
)

urlpatterns = [
    path("create_post/", PostsCreateView.as_view(), name="create_post"),
    path("update_post/<int:pk>/", PostsUpdateView.as_view(), name="update_post"),
    path("detele_post/<int:pk>/", PostsDeleteView.as_view(), name="detele_post"),
    path("detail_post/<int:pk>/", PostsDetailView.as_view(), name="detail_post"),
    path("list_post/", PostsListView.as_view(), name="list_post"),
]

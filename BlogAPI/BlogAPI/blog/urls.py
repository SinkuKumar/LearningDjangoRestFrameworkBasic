from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
    path("users/", views.UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    path("blogs/", views.BlogList.as_view(), name="blog-list"),
    path("blogs/<int:pk>/", views.BlogDetail.as_view(), name="blog-detail"),
    path("comments/", views.CommentList.as_view(), name="comment-list"),
    path("comments/<int:pk>/", views.CommentDetail.as_view(), name="comment-detail"),
    path("likes/", views.LikeList.as_view(), name="like-list"),
    path("likes/<int:pk>/", views.LikeDetail.as_view(), name="like-detail"),
    path("dislikes/", views.DislikeList.as_view(), name="dislike-list"),
    path("dislikes/<int:pk>/", views.DislikeDetail.as_view(), name="dislike-detail"),
]

from blog.models import Blog, Comment, Like, Dislike
from blog.serializers import BlogSerializer, CommentSerializer, LikeSerializer, DislikeSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BlogList(generics.ListCreateAPIView):
    """
    API endpoint that allows blogs to be viewed or created.
    """

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a single blog to be viewed, edited, or deleted.
    """

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentList(generics.ListCreateAPIView):
    """
    API endpoint that allows comments to be viewed or created.
    """

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a single comment to be viewed, edited, or deleted.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LikeList(generics.ListCreateAPIView):
    """
    API endpoint that allows likes to be viewed or created.
    """

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a single like to be viewed, edited, or deleted.
    """

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DislikeList(generics.ListCreateAPIView):
    """
    API endpoint that allows dislikes to be viewed or created.
    """

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    queryset = Dislike.objects.all()
    serializer_class = DislikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DislikeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a single dislike to be viewed, edited, or deleted.
    """

    queryset = Dislike.objects.all()
    serializer_class = DislikeSerializer

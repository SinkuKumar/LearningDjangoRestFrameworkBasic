from todo.models import ToDo
from todo.serializers import ToDoSerializer, UserSerializer
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


class ToDoList(generics.ListCreateAPIView):
    """
    API endpoint that allows to-do items to be viewed or created.
    """

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ToDoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a single to-do item to be viewed, edited, or deleted.
    """

    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

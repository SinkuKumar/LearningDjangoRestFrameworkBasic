from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from todo import views


urlpatterns = [
    path("users/", views.UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    path("todos/", views.ToDoList.as_view(), name="todo-list"),
    path("todos/<int:pk>/", views.ToDoDetail.as_view(), name="todo-detail"),
]

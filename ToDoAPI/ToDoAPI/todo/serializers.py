from todo.models import ToDo
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model

    :Attributes:
    username (str): The username of the user
    todos (list of ToDo): The to-do items the user has created
    """

    todos = serializers.PrimaryKeyRelatedField(many=True, queryset=ToDo.objects.all())

    class Meta:
        """
        Metadata for the UserSerializer

        :Attributes:
        model (User): The User model
        fields (list of str): The fields to include in the serialized data
        """

        model = User
        fields = ["id", "username", "todos"]


class ToDoSerializer(serializers.ModelSerializer):
    """
    Serializer for the ToDo model

    :Attributes:
    title (str): The title of the to-do item
    description (str): The description of the to-do item
    completed (bool): Whether the to-do item is completed
    created_at (datetime): The date and time the to-do item was created
    updated_at (datetime): The date and time the to-do item was last updated
    owner (User): The user who owns the to-do item
    """

    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        """
        Metadata for the ToDoSerializer

        :Attributes:
        model (ToDo): The ToDo model
        fields (list of str): The fields to include in the serialized data
        """

        model = ToDo
        fields = "__all__"

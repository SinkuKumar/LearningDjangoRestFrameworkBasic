from django.db import models
from django.contrib import auth


class ToDo(models.Model):
    """
    Model for a to-do item

    :Attributes:
    title (str): The title of the to-do item
    description (str): The description of the to-do item
    completed (bool): Whether the to-do item is completed
    created_at (datetime): The date and time the to-do item was created
    updated_at (datetime): The date and time the to-do item was last updated
    owner (User): The user who owns the to-do item

    :Methods:
    __str__: Returns the title of the to-do item
    """

    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey("auth.User", related_name="todos", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

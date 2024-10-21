from django.db import models
from django.contrib import auth


class Blog(models.Model):
    """
    Model for a blog post

    :Attributes:
    title (str): The title of the blog post
    content (str): The content of the blog post
    date_created (datetime): The date and time the blog post
    owner (User): The owner of the blog

    :Methods:
    __str__: Returns the title of the blog post
    """

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey("auth.User", related_name="blogs", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Model for a comment on a blog post

    :Attributes:
    blog (Blog): The blog post the comment is on
    content (str): The content of the comment
    date_created (datetime): The date and time the comment was created
    owner (User): The owner of the comment

    :Methods:
    __str__: Returns the content of the comment
    """

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey("auth.User", related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Like(models.Model):
    """
    Model for a like on a blog post

    :Attributes:
    blog (Blog): The blog post the like is on
    date_created (datetime): The date and time the like was created
    owner (User): The owner of the like

    :Methods:
    __str__: Returns the title of the blog post
    """

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey("auth.User", related_name="likes", on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.title


class Dislike(models.Model):
    """
    Model for a dislike on a blog post

    :Attributes:
    blog (Blog): The blog post the dislike is on
    date_created (datetime): The date and time the dislike was created
    owner (User): The owner of the dislike

    :Methods:
    __str__: Returns the title of the blog post
    """

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey("auth.User", related_name="dislikes", on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.title

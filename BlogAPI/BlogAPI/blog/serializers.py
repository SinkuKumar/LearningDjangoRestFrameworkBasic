from blog import models
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model

    :Attributes:
    username (str): The username of the user
    blogs (list of Blog): The blogs the user has written
    likes (list of Like): The likes the user has given
    comments (list of Comment): The comments the user has written
    dislikes (list of Dislike): The dislikes the user has given
    """

    blogs = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Blog.objects.all())
    likes = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Like.objects.all())
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Comment.objects.all())
    dislikes = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Dislike.objects.all())

    class Meta:
        """
        Metadata for the UserSerializer

        :Attributes:
        model (User): The User model
        fields (list of str): The fields to include in the serialized data
        """

        model = User
        fields = ["id", "username", "blogs", "likes", "comments", "dislikes"]


class BlogSerializer(serializers.ModelSerializer):
    """
    Serializer for the Blog model

    :Attributes:
    title (str): The title of the blog post
    content (str): The content of the blog post
    date_created (datetime): The date and time the blog post was created

    :Methods:
    __str__: Returns the title of the blog post
    """

    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        """
        Metadata for the BlogSerializer

        :Attributes:
        model (Blog): The Blog model
        fields (list of str): The fields to include in the serialized data
        """

        model = models.Blog
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model

    :Attributes:
    blog (Blog): The blog post the comment is on
    content (str): The content of the comment
    date_created (datetime): The date and time the comment was created

    :Methods:
    __str__: Returns the content of the comment
    """

    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        """
        Metadata for the CommentSerializer

        :Attributes:
        model (Comment): The Comment model
        fields (list of str): The fields to include in the serialized data
        """

        model = models.Comment
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model

    :Attributes:
    blog (Blog): The blog post the like is on
    date_created (datetime): The date and time the like was created

    :Methods:
    __str__: Returns the title of the blog post
    """

    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        """
        Metadata for the LikeSerializer

        :Attributes:
        model (Like): The Like model
        fields (list of str): The fields to include in the serialized data
        """

        model = models.Like
        fields = "__all__"


class DislikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Dislike model

    :Attributes:
    blog (Blog): The blog post the dislike is on
    date_created (datetime): The date and time the dislike was created

    :Methods:
    __str__: Returns the title of the blog post
    """

    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        """
        Metadata for the DislikeSerializer

        :Attributes:
        model (Dislike): The Dislike model
        fields (list of str): The fields to include in the serialized data
        """

        model = models.Dislike
        fields = "__all__"

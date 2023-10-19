from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Rating

class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User.

    Args:
        serializers ([type]): Основной класс сериализатора DRF.

    Returns:
        [type]: Сериализованный объект пользователя.
    """

    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PostSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Post.

    Args:
        serializers ([type]): Основной класс сериализатора DRF.

    Returns:
        [type]: Сериализованный объект поста.
    """

    author = UserSerializer(read_only=True)  

    class Meta:
        model = Post
        fields = ['id', 'author', 'topic', 'content']

class RatingSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Rating.

    Args:
        serializers ([type]): Основной класс сериализатора DRF.

    Returns:
        [type]: Сериализованный объект рейтинга.
    """

    user = UserSerializer(read_only=True)  
    post = PostSerializer(read_only=True)  

    class Meta:
        model = Rating
        fields = ['id', 'user', 'post', 'stars']

from rest_framework import generics, permissions
from rest_framework import viewsets
from .models import Post, Rating
from .serializers import UserSerializer, PostSerializer, RatingSerializer
from django.contrib.auth.models import User
class UserListView(viewsets.ModelViewSet):
    """
    API-представление для просмотра и создания пользователей.

    Args:
        generics.ListCreateAPIView: Основной класс представления DRF.

    Attributes:
        queryset (QuerySet): Набор всех пользователей.
        serializer_class (UserSerializer): Сериализатор для модели User.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostListView(viewsets.ModelViewSet):
    """
    API-представление для просмотра и создания постов.

    Args:
        generics.ListCreateAPIView: Основной класс представления DRF.

    Attributes:
        queryset (QuerySet): Набор всех постов.
        serializer_class (PostSerializer): Сериализатор для модели Post.
        permission_classes (list): Разрешения доступа к представлению.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Создает новый пост и устанавливает текущего пользователя как автора.

        Args:
            serializer: Сериализатор, используемый для создания поста.

        Returns:
            None
        """
        serializer.save(author=self.request.user)

class RatingListView(viewsets.ModelViewSet):
    """
    API-представление для просмотра и создания рейтингов.

    Args:
        generics.ListCreateAPIView: Основной класс представления DRF.

    Attributes:
        queryset (QuerySet): Набор всех рейтингов.
        serializer_class (RatingSerializer): Сериализатор для модели Rating.
        permission_classes (list): Разрешения доступа к представлению.
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Создает новый рейтинг и устанавливает текущего пользователя как оценивающего.

        Args:
            serializer: Сериализатор, используемый для создания рейтинга.

        Returns:
            None
        """
        serializer.save(user=self.request.user)

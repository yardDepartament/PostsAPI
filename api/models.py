from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


    
class Post(models.Model):
    """
    Модель для представления постов.

    Атрибуты:
        author (User): Пользователь, который написал пост.
        topic (str): Тема поста.
        content (str): Содержание поста.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        """
        Возвращает строковое представление объекта Post.

        Пример:
            "Пост с темой: Заголовок поста"
        """
        return f"Пост с темой: {self.topic}"

    def get_rating(self):
        """
        Возвращает средний рейтинг поста.

        Возвращает:
            float: Средний рейтинг поста.
        """
        ratings = Rating.objects.filter(post=self)
        total_stars = sum([rating.stars for rating in ratings])
        if ratings:
            return total_stars / len(ratings)
        return 0
    
    
class Rating(models.Model):
    """
    Модель для представления рейтинга.

    Атрибуты:
        user (User): Пользователь, который оценил пост.
        post (Post): Пост, который оценивали.
        stars (int): Количество звезд, от 1 до 5.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост")
    stars = models.IntegerField(verbose_name="Рейтинг")

    def __str__(self):
        """
        Возвращает строковое представление объекта Rating.

        Пример:
            "Рейтинг поста: 5 зв."
        """
        return f"Рейтинг поста: {self.stars} зв."
    
    def clean(self):
        """
        Метод для валидации количества звёзд (1-5)
        
        Raises:
            ValidationError: _description_
        """
        if self.stars < 1 or self.stars > 5:
            raise ValidationError('Количество звезд должно быть от 1 до 5.')

    def save(self, *args, **kwargs):
        """
        Переопределение метода save для обновления рейтинга поста.
        """
        super(Rating, self).save(*args, **kwargs)
        self.post.save()
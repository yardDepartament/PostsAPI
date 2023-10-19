from django.urls import path
from .views import UserListView, PostListView, RatingListView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('ratings/', RatingListView.as_view(), name='rating-list'),
]
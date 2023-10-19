from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserListView, PostListView, RatingListView

router = DefaultRouter()
router.register(r'users', UserListView, basename='user')
router.register(r'posts', PostListView, basename='post')
router.register(r'ratings', RatingListView, basename='rating')

urlpatterns = [
    path('', include(router.urls)),
]

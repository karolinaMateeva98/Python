from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'hashtags', views.HashtagViewSet)

urlpatterns = [
    path('', include(router.urls)), 
]

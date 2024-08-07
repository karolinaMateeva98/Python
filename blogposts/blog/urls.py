from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, RegisterView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register')

    # path('', views.PostList.as_view(), name='home'),
    # path('<slug:slug>/', views.post_detail, name='post_detail'),
    # path('post/<slug:slug>/upvote/', views.upvote_post, name='upvote_post'),
    # path('post/<slug:slug>/downvote/', views.downvote_post, name='downvote_post'),
    # path('post/create/', views.post_create, name='post_create'),  
]

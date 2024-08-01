from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/upvote/', views.upvote_post, name='upvote_post'),
    path('post/<slug:slug>/downvote/', views.downvote_post, name='downvote_post'),
    path('post/create/', views.post_create, name='post_create'),  
]

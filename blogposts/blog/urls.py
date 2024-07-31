from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # path('user/', views.PostList.as_view(), name='user'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    
]

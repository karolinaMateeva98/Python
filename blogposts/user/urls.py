from django.urls import path, include
from django.conf import settings
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.user_login, name ='login'),
    path('logout/', views.user_logout, name ='logout'),
    path('register/', views.RegisterView.as_view(), name ='register'),
]

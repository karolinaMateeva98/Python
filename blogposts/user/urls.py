from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth

urlpatterns = [
	path('', views.index, name ='index'),
    path('login/', views.user_login, name ='login'),
    path('logout/', views.user_logout, name ='logout'),
    path('register/', views.register, name ='register'),
]

from django.contrib import admin
from django.urls import path, include
from django.urls import include, path
from blog import views
from user import views
from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = [
    path('', include('blog.urls')),
    path('auth/', include('user.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

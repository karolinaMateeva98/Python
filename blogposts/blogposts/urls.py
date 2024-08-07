from django.contrib import admin
from django.urls import path, include
from django.urls import include, path
from blog import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include('blog.urls')),
    path('users/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

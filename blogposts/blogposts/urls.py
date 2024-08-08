from django.contrib import admin
from django.urls import path, include
from django.urls import include, path


urlpatterns = [
    path('', include('blog.urls')),
    path('auth/', include('user.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

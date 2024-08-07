from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.permissions import AllowAny
from user.models import BlogUser
from rest_framework import generics, viewsets, permissions
from .serializers import UserSerializer


def index(request):
    return render(request, 'user/index.html', {'title': 'index'})

class RegisterView(generics.CreateAPIView):
    queryset = BlogUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BlogUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, f'Invalid username or password.')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form, 'title': 'Log in'})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('login')

from .permissions import IsAdminOrCommentCreator, IsAdminOrOwner, IsPostCreatorOrAdmin
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import Post, Hashtag, Comment
from .serializers import PostSerializer, HashtagSerializer, CommentSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwner]

    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class HashtagViewSet(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    # permission_classes = [permissions.IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({'detail': 'You do not have permission to perform this action.'}, status=403)
        return super().destroy(request, *args, **kwargs)
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminOrCommentCreator]
        elif self.action == 'delete':
            self.permission_classes = [IsPostCreatorOrAdmin]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(name=self.request.user.username)

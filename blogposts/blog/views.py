from itertools import count
from .pagination import PostPagination
from .permissions import IsAdminOrCommentCreator, IsAdminOrOwner, IsPostCreatorOrAdmin
from rest_framework import permissions, viewsets, filters, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment, Hashtag, Vote
from .serializers import PostSerializer, CommentSerializer, HashtagSerializer

class HomeViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_on')
    serializer_class = PostSerializer
    pagination_class = PostPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['created_on']
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwner]
    filterset_fields = ['hashtags']

    def get_queryset(self):
        queryset = super().get_queryset()
        hot = self.request.query_params.get('hot', None)
        if hot:
            queryset = queryset.annotate(num_comments=count('comments')).filter(upvotes__gte=5, num_comments__gte=2)
        return queryset

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_on')
    serializer_class = PostSerializer
    pagination_class = PostPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['created_on']
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwner]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        post = self.get_object()
        post.vote(request.user, Vote.UPVOTE)
        return Response({'status': 'post upvoted'})

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        post = self.get_object()
        post.vote(request.user, Vote.DOWNVOTE)
        return Response({'status': 'post downvoted'})

class HashtagViewSet(mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    permission_classes = [permissions.IsAdminUser]
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminOrCommentCreator]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminOrCommentCreator]
        elif self.action == 'delete':
            self.permission_classes = [IsPostCreatorOrAdmin]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
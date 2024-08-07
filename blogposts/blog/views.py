from .permissions import IsAdminOrCommentCreator, IsAdminOrOwner, IsPostCreatorOrAdmin, IsAdminOrReadOnly
from rest_framework import permissions, viewsets, filters, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment, Hashtag, Vote
from .serializers import PostSerializer, CommentSerializer, HashtagSerializer

class PostPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_on')
    serializer_class = PostSerializer
    pagination_class = PostPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['created_on']
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwner]
    
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     hot = self.request.query_params.get('hot', None)
    #     if hot:
    #         queryset = queryset.filter(votes__gte=5, comments__gte=2)
    #     return queryset

    # def perform_create(self, serializer):
    #     if len(self.request.data.get('hashtags', [])) > 10:
    #         raise serializers.ValidationError("You can add up to 10 hashtags.")
    #     serializer.save(author=self.request.user)
        
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
    permission_classes = [IsAdminOrReadOnly]
    
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

from rest_framework import serializers
from .models import Post, Comment, Hashtag, Vote
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'links', 'hashtags']
        read_only_fields = ['author', 'created_on']
        
    def get_upvotes(self, obj):
        return obj.votes.filter(vote=Vote.UPVOTE).count()

    def get_downvotes(self, obj):
        return obj.votes.filter(vote=Vote.DOWNVOTE).count()

    def get_total_votes(self, obj):
        return self.get_upvotes(obj) + self.get_downvotes(obj)

    def get_comments(self, obj):
        return obj.comments.count()
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'body', 'post']
        read_only_fields = ['created_on', 'author']
    
    def create(self, validated_data):
        comment = Comment.objects.create(**validated_data)
        return comment
        
        
class HashtagSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    
    class Meta:
        model = Hashtag
        fields = ['id', 'name', 'posts']
        
        
class VoteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='author.username')
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Vote
        fields = ['id', 'user', 'post', 'value']
        read_only_fields = ['user']

    def validate(self, data):
        user = self.context.get('user')
        post = data.get('post')
        value = data.get('value')
        
        if Vote.objects.filter(user=user, post=post, value=value).exists():
            raise serializers.ValidationError('User can vote only once for a single post.')
        return data
    
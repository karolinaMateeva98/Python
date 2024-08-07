from rest_framework import serializers
from .models import Post, Comment, Hashtag, Vote
    
class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'
        
    def get_upvotes(self, obj):
        return obj.votes.filter(vote=Vote.UPVOTE).count()

    def get_downvotes(self, obj):
        return obj.votes.filter(vote=Vote.DOWNVOTE).count()

    def get_total_votes(self, obj):
        return self.get_upvotes(obj) - self.get_downvotes(obj)

    def get_comments(self, obj):
        return obj.comments.count()
    
    # def create(self, validated_data):
    #     hashtags_data = validated_data.pop('hashtags')
    #     post = Post.objects.create(**validated_data)
    #     for hashtag_data in hashtags_data:
    #         hashtag, created = Hashtag.objects.get_or_create(**hashtag_data)
    #         post.hashtags.add(hashtag)
    #     return post

    # def update(self, instance, validated_data):
    #     hashtags_data = validated_data.pop('hashtags')
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.save()

    #     # Update hashtags
    #     instance.hashtags.clear()
    #     for hashtag_data in hashtags_data:
    #         hashtag, created = Hashtag.objects.get_or_create(**hashtag_data)
    #         instance.hashtags.add(hashtag)

    #     return instance
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
        
class HashtagSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    
    class Meta:
        model = Hashtag
        fields = ['id', 'name', 'posts']
        
        
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'
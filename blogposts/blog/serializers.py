from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Post, Hashtag, Comment

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    hashtags = HashtagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = '__all__'
    
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
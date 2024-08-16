from rest_framework import serializers
from user.models import BlogUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = BlogUser
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = BlogUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
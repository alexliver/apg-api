from rest_framework import serializers
from post.models import Post, Avatar
from django.contrib.auth.models import User

class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = ['image']

class UserSerializer(serializers.ModelSerializer):
    avatar = AvatarSerializer(read_only=True, many=False)
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'avatar')

class PostSerializer(serializers.ModelSerializer):
    #writer = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=User.objects.all())
    writer = UserSerializer(read_only=False, many=False)
    class Meta:
        model = Post
        fields = ('pk', 'writer', 'title', 'content', 'created_at')



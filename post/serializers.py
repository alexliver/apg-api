from rest_framework import serializers
from post.models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    writer = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=User.objects.all())
    class Meta:
        model = Post
        fields = ('pk', 'writer', 'title', 'content', 'created_at')


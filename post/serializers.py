from rest_framework import serializers
from post.models import Post, Avatar, Reply, IRepliable
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

class ReplySerializer(serializers.ModelSerializer):
    writer = UserSerializer(read_only=True, many=False)
    writerID = serializers.PrimaryKeyRelatedField(source='writer', many=False, read_only=False, queryset=User.objects.all())
    to = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=IRepliable.objects.all())
    class Meta:
        model = Reply
        fields = ('pk', 'writer', 'writerID', 'content', 'created_at', 'replies', 'to')
    def get_fields(self):
        fields = super(ReplySerializer, self).get_fields()
        fields['replies'] = ReplySerializer(many=True, read_only=True)
        return fields


class PostSerializer(serializers.ModelSerializer):
    writer = UserSerializer(read_only=True, many=False)
    replies = ReplySerializer(read_only=True, many=True)
    class Meta:
        model = Post
        fields = ('pk', 'writer', 'title', 'content', 'created_at', 'replies')



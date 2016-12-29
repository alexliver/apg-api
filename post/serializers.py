from rest_framework import serializers
from post.models import Post, Avatar, Reply, IRepliable, Category
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
    writer = UserSerializer(read_only=False, many=False,
            default=serializers.CurrentUserDefault()
            )
    '''
    writerID = serializers.PrimaryKeyRelatedField(source='writer', many=False, read_only=False, 
            default=serializers.CurrentUserDefault().pk,
            queryset=User.objects.all())
    '''
    to = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=IRepliable.objects.all())
    class Meta:
        model = Reply
        fields = ('pk', 'writer', 'content', 'created_at', 'replies', 'to')
    def get_fields(self):
        fields = super(ReplySerializer, self).get_fields()
        fields['replies'] = ReplySerializer(many=True, read_only=True)
        return fields


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'name', 'iconType')


class PostSerializer(serializers.ModelSerializer):
    writer = UserSerializer(read_only=True, many=False)
    replies = ReplySerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True, many=False)
    class Meta:
        model = Post
        fields = ('pk', 'writer', 'title', 'content', 'created_at', 'replies', 'category')



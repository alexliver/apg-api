from django.shortcuts import render
from post.models import Post, Reply
from post.serializers import PostSerializer, ReplySerializer
from rest_framework import generics
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ReplyList(generics.ListCreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

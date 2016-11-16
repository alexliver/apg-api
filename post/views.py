from django.shortcuts import render
from post.models import Post
from post.serializers import PostSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

from django.shortcuts import render
from post.models import Post, Reply, Category
from post.serializers import PostSerializer, ReplySerializer, UserSerializer, CategorySerializer
from rest_framework import generics
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.authtoken import views as authViews

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryPostList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        categoryID = self.kwargs['categoryID']
        return Post.objects.filter(category__pk=categoryID)
        
class ReplyList(generics.ListCreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

class ObtainAuthToken(authViews.ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = authViews.ObtainAuthToken.post(self, request, *args, **kwargs)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        data = response.data
        data['user'] = UserSerializer(user).data
        return Response(data)

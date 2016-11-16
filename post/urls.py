from django.conf.urls import include, url
from post import views
from post.models import Post
from django.contrib import admin

admin.site.register(Post)
urlpatterns = [
    url(r'^post/$', views.PostList.as_view()),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
]

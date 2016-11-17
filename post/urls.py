from django.conf.urls import include, url
from post import views
from post.models import Post, Avatar
from django.contrib import admin

admin.site.register(Post)
admin.site.register(Avatar)
urlpatterns = [
    url(r'^post/$', views.PostList.as_view()),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
]

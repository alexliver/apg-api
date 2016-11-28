from django.conf.urls import include, url
from post import views
from post.models import Post, Avatar, Category
from django.contrib import admin

admin.site.register(Post)
admin.site.register(Avatar)
admin.site.register(Category)
urlpatterns = [
    url(r'^category/$', views.CategoryList.as_view()),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
    url(r'^post/$', views.PostList.as_view()),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
    url(r'^categoryPostList/(?P<categoryID>[0-9]+)/$', views.CategoryPostList.as_view()),
    url(r'^reply/$', views.ReplyList.as_view()),
    url(r'^reply/(?P<pk>[0-9]+)/$', views.ReplyDetail.as_view()),
    url(r'^login/$', views.ObtainAuthToken.as_view()),
]

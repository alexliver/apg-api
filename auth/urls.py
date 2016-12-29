from django.conf.urls import include, url
from auth import views

urlpatterns = [
    url(r'^sign_up/$', views.SignUp.as_view(), name="sign_up"),
]

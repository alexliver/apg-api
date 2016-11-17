from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class IRepliable(models.Model):
  pass

class Post(IRepliable):  
  writer = models.ForeignKey(User, related_name='posts', blank = False)  
  title = models.TextField(blank = False)
  content = models.TextField(blank = True)
  created_at = models.DateTimeField(auto_now_add=True)

class Reply(IRepliable): 
  to = models.ForeignKey(IRepliable, related_name='replies')
  writer = models.ForeignKey(User, related_name='replies', blank = False)  
  content = models.TextField(blank = True)
  created_at = models.DateTimeField(auto_now_add=True)

class Avatar(models.Model): 
  image = models.ImageField(upload_to='media/avatars/', null=False)
  user = models.OneToOneField(User, related_name="avatar", null = False)

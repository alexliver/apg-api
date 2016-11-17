from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):  
  writer = models.ForeignKey(User, related_name='posts', blank = False)  
  title = models.TextField(blank = False)
  content = models.TextField(blank = True)
  created_at = models.DateTimeField(auto_now_add=True)

class Avatar(models.Model): 
  image = models.ImageField(upload_to='media/avatars/', null=False)
  user = models.OneToOneField(User, related_name="avatar", null = False)

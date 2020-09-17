from django.db import models
from datetime import datetime

class BlogPost(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    blogpost = models.ForeignKey(BlogPost, blank=True, null=True, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name
    

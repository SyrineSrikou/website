from django.db import models
from datetime import datetime

class BlogPost(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

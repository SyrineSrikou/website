from django.db import models
from datetime import datetime
from services.models import Service

class Reference(models.Model):
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

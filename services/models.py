from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    def description_as_list(self):
        return self.description.split('\n')
 
    def __str__(self):
        return self.name
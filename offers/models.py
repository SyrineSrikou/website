from django.db import models
from datetime import datetime

class Offer(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100, blank=True)
    postdate = models.DateTimeField(default=datetime.now, blank=True)
    deadline = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField(blank=True)
    responsibility = models.TextField(blank=True)
    qualifications = models.TextField(blank=True)
    offer_nature = models.CharField(max_length=100, blank=True)
    Vacancy = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")

    def description_as_list(self):
        return self.description.split('\n')
    def responsibility_as_list(self):
        return self.description.split('\n')
    def qualifications_as_list(self):
        return self.description.split('\n')
    
    def __str__(self):
        return self.title

class Application(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    cv = models.FileField(blank=True, null=True, upload_to="CV/%Y/%m/%d/")
    message = models.TextField(blank=True)
    application_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    facebook = models.CharField(max_length=200, blank=True)
    instagram = models.CharField(max_length=200, blank=True)
    twiter = models.CharField(max_length=200, blank=True)
    linkenin = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")


    def __str__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")


    def __str__(self):
        return self.name
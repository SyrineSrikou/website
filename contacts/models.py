from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=50)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name


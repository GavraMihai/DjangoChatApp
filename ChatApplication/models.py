from django.db import models
from datetime import datetime


# Create your models here.
class Account(models.Model):
    userName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Room(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50, null=True)


class Message(models.Model):
    value = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now, blank=True)
    room = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/images/uploads', null=True)

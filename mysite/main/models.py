from django.db import models
from datetime import datetime

# Create your models here.
class Tutorials(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("date published",default=datetime.now())

class Essays(models.Model):
    essay_title = models.CharField(max_length=200)
    essay_content = models.TextField()
    essay_published = models.DateTimeField("date published",default=datetime.now())

class Usernames(models.Model):
    user_name = models.CharField(max_length=200)
    age = models.IntegerField()
    occupation = models.TextField()

class Vehicles(models.Model):
    vehicle_name = models.CharField(max_length=20)
    reg_no = models.TextField()
    yom = models.IntegerField()
    

def __str__(self):
    return self.tutorial_title

def __str__(self):
    return self.essay_title

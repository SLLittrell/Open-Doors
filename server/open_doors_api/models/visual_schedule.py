from django.db import models 
from django.contrib.auth.models import User
from django.core.files import File


class VisualSchedule(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    activity_1 = models.CharField(max_length=200)
    image_1 = models.TextField()
    activity_2 = models.CharField(max_length=200)
    image_2 = models.TextField()
    activity_3 = models.CharField(max_length=200)
    image_3 = models.TextField()
    activity_4 = models.CharField(max_length=200)
    image_4 = models.TextField()
    activity_5 = models.CharField(max_length=200)
    image_5 = models.TextField()
    activity_6 = models.CharField(max_length=200)
    image_6 = models.TextField()
    activity_7 = models.CharField(max_length=200)
    image_7 = models.TextField()
    activity_8 = models.CharField(max_length=200)
    image_8 = models.TextField()
    activity_9 = models.CharField(max_length=200)
    image_9 = models.TextField()
    activity_10 = models.CharField(max_length=200)
    image_10 = models.TextField()
    



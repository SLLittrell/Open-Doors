from django.db import models 
from django.contrib.auth.models import User
from django.db.models.fields import BooleanField


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    publication_date = models.DateTimeField(auto_now_add=True)
    image_url = models.CharField(max_length=500)
    social_story = models.ForeignKey("SocialStory", on_delete=models.CASCADE, null=True, blank=True)
    visual_schedule = models.ForeignKey("VisualSchedule", on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    approved = models.BooleanField()
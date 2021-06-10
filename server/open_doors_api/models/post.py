from django.db import models 
from django.contrib.auth.models import User
from django.db.models.fields import BooleanField
from django.utils import timezone

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    publication_date = models.DateTimeField()
    image_url = models.CharField(max_length=250)
    social_story = models.ForeignKey("SocialStory", on_delete=models.CASCADE, null=True)
    visual_schedule = models.ForeignKey("VisualSchedule", on_delete=models.CASCADE, null=True)
    # image_url = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    content = models.TextField()
    approved = models.BooleanField()
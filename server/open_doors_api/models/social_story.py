from django.db import models 
from django.contrib.auth.models import User
from django.core.files import File


class SocialStory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attraction = models.CharField(max_length=50)
    publication_date = models.DateTimeField(auto_now_add=True)
    titlepage = models.TextField()
    title_image = models.TextField()
    page_1_text = models.TextField()
    page_1_image = models.TextField()
    page_2_text = models.TextField()
    page_2_image = models.TextField()
    page_3_text = models.TextField()
    page_3_image = models.TextField()
    page_4_text = models.TextField()
    page_4_image = models.TextField()
    page_5_text = models.TextField()
    page_5_image = models.TextField()
    page_6_text = models.TextField()
    page_6_image = models.TextField()
    page_7_text = models.TextField()
    page_7_image = models.TextField()
    page_8_text = models.TextField()
    page_8_image = models.TextField()
    page_9_text = models.TextField()
    page_9_image = models.TextField()
    page_10_text = models.TextField()
    page_10_image = models.TextField()

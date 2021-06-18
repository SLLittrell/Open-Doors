from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import action
import datetime
from open_doors_api.models import SocialStory, OpenUser


class PostView(ViewSet):
    def create(self, request):
        """Ensure client can create a story"""
        user = OpenUser.objects.get(user=request.auth.user)
        story =SocialStory()
        story.titlepage = (request.data['title'])
        story.title_image = (request.data['title_image'])
        story.page_1_text = (request.data['page_1_text'])
        story.page_1_image = (request.data['page_1_image'])
        story.page_2_text = (request.data['page_2_text'])
        story.page_2_image = (request.data['page_2_image'])
        story.page_3_text = (request.data['page_3_text'])
        story.page_3_image = (request.data['page_3_image'])
        story.page_4_text = (request.data['page_4_text'])
        story.page_4_image = (request.data['page_4_image'])
        story.page_5_text = (request.data['page_5_text'])
        story.page_5_image = (request.data['page_5_image'])
        story.page_6_text = (request.data['page_6_text'])
        story.page_6_image = (request.data['page_6_image'])
        story.page_7_text = (request.data['page_7_text'])
        story.page_7_image = (request.data['page_7_image'])
        story.page_8_text = (request.data['page_8_text'])
        story.page_8_image = (request.data['page_8_image'])
        story.page_9_text = (request.data['page_9_text'])
        story.page_9_image = (request.data['page_9_image'])
        story.page_10_text = (request.data['page_10_text'])
        story.page_10_image = (request.data['page_10_image'])

        try:
            story.save()
            serializer = StorySerializer(story, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


class StoryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username']


class StoryOpenUserSerializer(serializers.ModelSerializer):

    user = StoryUserSerializer(many=False)
    class Meta:
        model = OpenUser
        fields = ['user']

class StorySerializer(serializers.ModelSerializer):

    user = StoryUserSerializer(many=False)
    class Meta:
        model = SocialStory
        fields = ['user', 'title', 'pdf']
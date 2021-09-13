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


class SocialStoryView(ViewSet):
    def create(self, request):
        """Ensure client can create a story"""
        user = OpenUser.objects.get(user=request.auth.user)
        story =SocialStory()
        story.user =user.user
        story.titlepage = (request.data['titlepage'])
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
        if request.data['attraction'] is not None:
            story.attraction = (request.data["attraction"])
        if request.data['page_6_text'] is not None:
            story.page_6_text =(request.data["page_6_text"])
        if request.data['page_6_image'] is not None:
            story.page_6_image =(request.data["page_6_image"])
        if request.data['page_7_text'] is not None:
            story.page_7_text =(request.data["page_7_text"])
        if request.data['page_7_image'] is not None:
            story.page_7_image =(request.data["page_7_image"])
        if request.data['page_8_text'] is not None:
            story.page_8_text =(request.data["page_8_text"])
        if request.data['page_8_image'] is not None:
            story.page_8_image =(request.data["page_8_image"])
        if request.data['page_9_text'] is not None:
            story.page_9_text =(request.data["page_9_text"])
        if request.data['page_9_image'] is not None:
            story.page_9_image =(request.data["page_9_image"])
        if request.data['page_10_text'] is not None:
            story.page_10_text =(request.data["page_10_text"])
        if request.data['page_10_image'] is not None:
            story.page_10_image =(request.data["page_10_image"])


        try:
            story.save()
            serializer = StorySerializer(story, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def list(self,request):
        """Handle GET requests to games resource
        Returns:
            Response -- JSON serialized list of games
        """
        story = SocialStory.objects.all()
        serializer = StorySerializer(
            story, many=True, context={'request': request})
        return Response(serializer.data)
    
    def retrieve(self,request, pk=None):
        """Handle GET requests to games resource
        Returns:
            Response -- JSON serialized list of games
        """
        try:
            story = SocialStory.objects.get(pk=pk)
            serializer = StorySerializer(
                story, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """
        user = OpenUser.objects.get(user=request.auth.user)
        story =SocialStory.objects.get(pk=pk)
        story.user =user.user
        story.titlepage = (request.data['titlepage'])
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
        if story.attraction is None:
            try: story.attraction = request.data["attraction"]
            except: story.attraction = None
        elif request.data['attraction'] is not None:
            story.attraction = request.data["attraction"]
        if story.page_6_text is None:
            try: story.page_6_text = request.data["page_6_text"]
            except: story.page_6_text = None
        elif request.data['page_6_text'] is not None:
            story.page_6_text = request.data["page_6_text"]
        if story.page_6_image is None:
            try: story.page_6_image = request.data["page_6_image"]
            except: story.page_6_image = None
        elif request.data['page_6_image'] is not None:
            story.page_6_image = request.data["page_6_image"]
        if story.page_7_text is None:
            try: story.page_7_text = request.data["page_7_text"]
            except: story.page_7_text = None
        elif request.data['page_7_text'] is not None:
            story.page_7_text = request.data["page_7_text"]
        if story.page_7_image is None:
            try: story.page_7_image = request.data["page_7_image"]
            except: story.page_7_image = None
        elif request.data['page_7_image'] is not None:
            story.page_7_image = request.data["page_7_image"]
        if story.page_8_text is None:
            try: story.page_8_text = request.data["page_8_text"]
            except: story.page_8_text = None
        elif request.data['page_8_text'] is not None:
            story.page_8_text = request.data["page_8_text"]
        if story.page_8_image is None:
            try: story.page_8_image = request.data["page_8_image"]
            except: story.page_8_image = None
        elif request.data['page_8_image'] is not None:
            story.page_8_image = request.data["page_8_image"]
        if story.page_9_text is None:
            try: story.page_9_text = request.data["page_9_text"]
            except: story.page_9_text = None
        elif request.data['page_9_text'] is not None:
            story.page_9_text = request.data["page_9_text"]
        if story.page_9_image is None:
            try: story.page_9_image = request.data["page_9_image"]
            except: story.page_9_image = None
        elif request.data['page_9_image'] is not None:
            story.page_9_image = request.data["page_9_image"]
        if story.page_10_text is None:
            try: story.page_10_text = request.data["page_10_text"]
            except: story.page_10_text = None
        elif request.data['page_10_text'] is not None:
            story.page_10_text = request.data["page_10_text"]
        if story.page_10_image is None:
            try: story.page_10_image = request.data["page_10_image"]
            except: story.page_10_image = None
        elif request.data['page_10_image'] is not None:
            story.page_10_image = request.data["page_10_image"]

        # Try/Except try to save new post instance and use serializer to convert to json
        try:
            story.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single post
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            story = SocialStory.objects.get(pk=pk)
            story.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except SocialStory.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
        fields = ['id','user','publication_date', 'attraction','titlepage',
                         'title_image',
                         'page_1_text',
                         'page_1_image',
                         'page_2_text',
                         'page_2_image',
                         'page_3_text',
                         'page_3_image',
                         'page_4_text',
                         'page_4_image',
                         'page_5_text',
                         'page_5_image',
                         'page_6_text',
                         'page_6_image',
                         'page_7_text',
                         'page_7_image',
                         'page_8_text',
                         'page_8_image',
                         'page_9_text',
                         'page_9_image',
                         'page_10_text',
                         'page_10_image']
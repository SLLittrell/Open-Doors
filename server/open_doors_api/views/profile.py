"""View module for handling requests about park areas"""
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from open_doors_api.models import OpenUser 


class ProfileView(ViewSet):
    """Users can see profile information"""
    def list(self, request):
        """Handle GET requests to profile resource
        Returns:
            Response -- JSON representation of user info and events
        """
        user = OpenUser.objects.get(user=request.auth.user)

        current_user = OpenUserSerializer(
            user, many=False, context={'request':request}
        )

        profile ={}
        profile['user'] = current_user.data

        return Response(profile)


class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for user's  related Django user"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')


class OpenUserSerializer(serializers.ModelSerializer):
    """JSON serializer for gamers"""
    user = UserSerializer(many=False)

    class Meta:
        model = OpenUser
        fields = ('user',)
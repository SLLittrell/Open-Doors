from open_doors_api.models import OpenUser
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.decorators import action
from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework import serializers
from django.contrib.auth.models import User


class OpenUserView(ViewSet):
    def list(self, request):
        users = OpenUser.objects.all()
        res = OpenUserSerializer(users, many=True)
        return Response(res.data)

    
    def retrieve(self, request, pk=None):
        """Handle GET requests for single user
        Returns:
            Response -- JSON serialized game instance
        """
        try:
          
            user = OpenUser.objects.get(pk=pk)
            serializer = OpenUserSerializer(user, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """
        user = User.objects.get(pk=pk)

        user.is_staff=request.data['is_staff']
        
        user.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')

class OpenUserSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False)
    class Meta:
        model = OpenUser
        fields = ('id', 'user')
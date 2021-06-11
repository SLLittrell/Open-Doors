import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch 

from django.http import HttpResponse
from rest_framework import serializers
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from open_doors_api.models import OpenUser, SocialStory


class StoryView(ViewSet):

    def create(self, request):
        """Ensure client can create a story"""
        Page1 = []
        title_image = []
        Page2 = []
        Page3 = []
        Page4 = []
        Page5 = []
        Page6 = []
        title = request.data['title']
        image = request.data['image']
        text = request.data['text']
        Page1.append(title)
        title_image.append(image)
        Page2.append(text)
        


        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
        textob = pdf.beginText()
        textob.setTextOrigin(inch, inch)
        textob.setFont("Helvetica", 14)

        for line in Page1:
            textob.textLine(line)

            
        pdf.drawText(textob)
    ########Image######
        for image in title_image:
            pdf.drawImage(image, 500, 100)
    #########Drawstring(text)##########


        pdf.showPage()

        pdf.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='story.pdf')
    # def create(self, request):
    #     """Handle POST operations
    #     Returns:
    #         Response -- JSON serialized post instance
    #     """
    #     user = User.objects.get(user=request.auth.user)

    #     data = request
            # title = row.data['title'],
            # image = row.data['image']
            # text = row.data ['text']

        # story = SocialStory()
        # story.title = request.data['title']
        # story.user = user
        # # story.pdf = generate_pdf
        
        # try:
        #     story.save()
        #     serializer = StorySerializer(story, context={'request': request})
        #     return Response(serializer.data)

        # except ValidationError as ex:
        #     return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

# class StoryUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'first_name', 'last_name', 'username']


# class StoryOpenUserSerializer(serializers.ModelSerializer):

#     user = StoryUserSerializer(many=False)
#     class Meta:
#         model = OpenUser
#         fields = ['user']

# class StorySerializer(serializers.ModelSerializer):

#     user = StoryOpenUserSerializer(many=False)
#     class Meta:
#         model = SocialStory
#         fields = ['user', 'title']


import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch 
from reportlab.lib import colors


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
    
        titlepage = (request.data['title'])
        title_image = (request.data['title_image'])
        page_1_text = (request.data['page_1_text'])
        page_1_image = (request.data['page_1_image'])
        


        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=(landscape(letter)))
        textob = pdf.beginText()
        textob.setTextOrigin(inch, inch)
        textob.setFont("Helvetica", 36,)

    ########TitleImage######
        pdf.drawImage(title_image, 20, 28, width=750, height=550)
    #########Title##########
        pdf.setFillColorRGB(255,255,255)
        pdf.rect(50, 50, 5*inch,1.5*inch, fill=1)
        
        textob.setFillColorRGB(0,0,0)
        textob.textLine(titlepage)
        pdf.drawText(textob)
       
        
        pdf.showPage()
    ######Page1########
        pdf.drawImage(page_1_image, 20, 28, width=750, height=550)

        pdf.setFillColorRGB(255,255,255)
        pdf.rect(50, 50, 9.5*inch,1.5*inch, fill=1)
        
        
        pdf.setFillColorRGB(0,0,0)
        pdf.setFont("Helvetica", 25,)
        pdf.drawString(60, 1.25*inch, page_1_text)
        
        pdf.showPage()
        
        pdf.save()
        
        buffer.seek(0)
        # pdf: bytes = buffer.getvalue()
        return FileResponse(buffer, as_attachment=True, filename='story.pdf')

        
        story = SocialStory()
        story.title = titlepage
        story.user = User.objects.get(id=request.auth.user_id)
        story.pdf.save('story.pdf', story, save=False)
        
    
        story.save()
           

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


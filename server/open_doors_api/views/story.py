import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch 
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, flowables

from django.core.files.base import ContentFile
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
        page_2_text = (request.data['page_2_text'])
        page_2_image = (request.data['page_2_image'])
        page_3_text = (request.data['page_3_text'])
        page_3_image = (request.data['page_3_image'])
        page_4_text = (request.data['page_4_text'])
        page_4_image = (request.data['page_4_image'])
        page_5_text = (request.data['page_5_text'])
        page_5_image = (request.data['page_5_image'])
        

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
        #####Page2#######
        pdf.drawImage(page_2_image, 20, 28, width=750, height=550)

        pdf.setFillColorRGB(255,255,255)
        pdf.rect(50, 50, 9.5*inch,1.5*inch, fill=1)
        
        
        pdf.setFillColorRGB(0,0,0)
        pdf.setFont("Helvetica", 25,)
        pdf.drawString(60, 1.25*inch, page_2_text)
        
        pdf.showPage()
        #####Page3#######
        pdf.drawImage(page_3_image, 20, 28, width=750, height=550)

        pdf.setFillColorRGB(255,255,255)
        pdf.rect(50, 50, 9.5*inch,1.5*inch, fill=1)
        
        
        pdf.setFillColorRGB(0,0,0)
        pdf.setFont("Helvetica", 25,)
        pdf.drawString(60, 1.25*inch, page_3_text)
        
        pdf.showPage()
        #####Page4#######
        pdf.drawImage(page_4_image, 20, 28, width=750, height=550)

        pdf.setFillColorRGB(255,255,255)
        pdf.rect(50, 50, 9.5*inch,1.5*inch, fill=1)
        
        
        pdf.setFillColorRGB(0,0,0)
        pdf.setFont("Helvetica", 25,)
        pdf.drawString(60, 1.25*inch, page_4_text)
        
        pdf.showPage()
        #####Page5#######
        pdf.drawImage(page_5_image, 20, 28, width=750, height=550)

        pdf.setFillColorRGB(255,255,255)
        pdf.rect(50, 50, 9.5*inch,1.5*inch, fill=1)
        
        
        pdf.setFillColorRGB(0,0,0)
        pdf.setFont("Helvetica", 25,)
        pdf.drawString(60, 1.25*inch, page_5_text)
        
        pdf.showPage()
        
        pdf.save()
        
        buffer.seek(0)
    
        return FileResponse(buffer, as_attachment=True, filename='story.pdf')
        

    def list(self,request):
        """Handle GET requests to games resource
        Returns:
            Response -- JSON serialized list of games
        """
        story = SocialStory.objects.all()
        serializer = StorySerializer(
            story, many=True, context={'request': request})
        return Response(serializer.data)
    # @action(methods=['post','get'], detail=True)
    # def save_pdf(self,request,pk=None):
    #     if request.method == "POST"
    # pdf_file = FileResponse(pdf, filename='story.pdf')
    # pdf: bytes= buffer.getvalue()
    # flowables =[]
    # doc = SimpleDocTemplate(buffer)
    # doc.build(flowables)

    # file_data = ContentFile(pdf)
    # user = OpenUser.objects.get(user=request.auth.user)
    # story = SocialStory()
    # story.title = titlepage
    # story.user = user.user
    # story.pdf.save('story.pdf', file_data, save=False)
    
    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="story.pdf"'
    
    # response.write(pdf_files)
    
    
    # FileResponse(pdf, filename='story.pdf')


    # pdf: bytes = buffer.getvalue()
    # pdf_file = FileResponse(buffer, as_attachment=True, filename='')
    

   
        #  
    
        
    def retrieve(self, request, pk=None):
        """Handle GET requests for single pdf story
        Returns:
            Response -- JSON serialized story instance
        """
        try:
            post = SocialStory.objects.get(pk=pk)

            pdf = self.request.query_params.get('pdf', None)

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="story.pdf"'
            
            response.write(pdf)
            
            
            return response

        
        except Exception as ex:
            serializer = StorySerializer(post, context={'request': request})
            return Response(serializer.data)
            

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


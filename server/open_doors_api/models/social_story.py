from django.db import models 
from django.contrib.auth.models import User
from django.core.files import File
# from .utils import render_to_pdf

class SocialStory(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='pdf/', null=True, blank=True)


# def generate_obj_pdf(instance_id):
#      obj = SocialStory.objects.get(id=instance_id)
#      context = {'instance': obj}
#      pdf = render_to_pdf('your/pdf/template.html', context)
#      filename = "YourPDF_Order{}.pdf" %(obj.slug)
#      obj.pdf.save(filename, File(BytesIO(pdf.content)))
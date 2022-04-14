from django.db import models
from django.urls import reverse
from uuid import uuid4
from django.db.models.signals import pre_save


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = "news_archive/{filename}".format(
        filename='{}.{}'.format(uuid4().hex, ext))
    # file_path = f"news_archive/{f'{uuid4().hex}.{ext}'}"
    # file_path = f"news_archive/{uuid4().hex}.{ext}"
    return file_path

class ProjectModel(models.Model):
    company = models.CharField(max_length=50, null=True, blank=True)
    founder = models.CharField(max_length=50, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)


    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.company)



    def get_absolute_url(self):
        return reverse("", args=[str(self.id)])




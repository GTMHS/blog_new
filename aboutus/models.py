from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class AboutUs(models.Model):
    content = RichTextUploadingField()


class HomePage(models.Model):
    content = RichTextUploadingField()


class Advantages(models.Model):
    content = RichTextUploadingField()

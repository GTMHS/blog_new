from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_type = models.CharField(max_length=20)
    content = RichTextUploadingField()

    class Meta:
        ordering = ['-product_name']
from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'content')

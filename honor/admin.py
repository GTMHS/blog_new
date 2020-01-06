from django.contrib import admin
from .models import Honor
# Register your models here.

@admin.register(Honor)
class HonorAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')

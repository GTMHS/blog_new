from django.contrib import admin
from .models import AboutUs, HomePage, Advantages

# Register your models here.
@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')


@admin.register(Advantages)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')

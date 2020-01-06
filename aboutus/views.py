from django.shortcuts import render_to_response,get_object_or_404
from .models import AboutUs, Advantages
# Create your views here.


def show_about_us(request):
    context = {}
    context['content'] = get_object_or_404(AboutUs, pk=1)
    return render_to_response('about_us.html', context)


def show_advantages(request):
    context = {}
    context['content'] = get_object_or_404(Advantages, pk=1)
    return render_to_response('advantages.html', context)

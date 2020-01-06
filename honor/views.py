from django.shortcuts import render_to_response,get_object_or_404
from .models import Honor
# Create your views here.


def show_honor(request):
    context = {}
    context['content'] = get_object_or_404(Honor, pk=1)
    return render_to_response('honor.html', context)


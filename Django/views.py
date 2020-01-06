from django.shortcuts import get_object_or_404, render_to_response
from aboutus.models import HomePage

def home(request):
    context = {}
    context['content'] = get_object_or_404(HomePage, pk=1)
    return render_to_response('home.html', context)


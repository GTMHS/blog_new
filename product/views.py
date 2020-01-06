from django.shortcuts import render_to_response, get_object_or_404
from .models import Product

# Create your views here.
def prodcut_list(request):
    context = {}
    context['products'] = Product.objects.all()
    # context['blogs'] = Product.objects.all()
    # context['blog_types'] = Product.product_type
    # context['blogs_count'] = Product.objects.all().count()
    return render_to_response('product_list.html', context)


# def prodcut_detail(request, blog_pk):
#     context = {}
#     context['blog'] = get_object_or_404(Product, pk=blog_pk)
#     return render_to_response('product_detail.html', context)

from django.shortcuts import render_to_response,get_object_or_404
from django.core.paginator import Paginator
from .models import Blog, BlogType


# Create your views here.
def blog_list(request):
    blog_all_list = Blog.objects.all()
    paginator = Paginator(blog_all_list, 10)  #每10页分一页
    page_num = request.GET.get('page', 1)  # 获取页码参数（GET）请求
    page_of_blogs = paginator.get_page(page_num)

    context = {}
    context['page_of_blogs'] = page_of_blogs
    context['blog_types'] = BlogType.objects.all()
    # context['blogs_count'] = Blog.objects.all().count()
    return render_to_response('blog_list.html', context)
    pass


def blog_detail(request, blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    return render_to_response('blog_detail.html', context)

def blogs_with_types(request,blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    context['blog_type'] = blog_type
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    return render_to_response('blogg_with_type.html', context)


from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')

    paginator = Paginator(blogs, 3)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'blog-list.html', {
        'page_obj': page_obj
    })
    
def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    blogs = list(
        Blog.objects.all()
        .order_by('-created_at')
        .values_list('id', flat=True)
    )

    current_index = blogs.index(blog.id)
    previous_blog_id = None
    next_blog_id = None

    if current_index > 0:
        previous_blog_id = blogs[current_index - 1]

    if current_index < len(blogs) - 1:
        next_blog_id = blogs[current_index + 1]

    return render(request, 'blog-detail.html', {
        'blog': blog,
        'previous_blog': previous_blog_id,
        'next_blog': next_blog_id,
    })
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Blog,Rates
from django.db.models import Avg
from django.http import JsonResponse

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
        
    # rate 
    user_rate = Rates.objects.filter(
        blog=blog,
        author=request.user
    ).exists()
    
    result = Rates.objects.filter(
        blog=blog
    ).aggregate(
        average=Avg('rate')
    )

    avg_rate = result['average']

    if avg_rate is None:
        avg_rate = 0

    avg_rate = round(avg_rate)

    return render(request, 'blog-detail.html', {
        'blog': blog,
        'previous_blog': previous_blog_id,
        'next_blog': next_blog_id,
        'user_rate': user_rate,
        'avg_rate': avg_rate,
    })
    
def blog_rate(request):
    if request.method == 'POST':
        blog_id = request.POST.get('blog_id')
        rate_value = request.POST.get('rate')
        
        try:
            blog = Blog.objects.get(id=blog_id)
            Rates.objects.create(
            blog_id=blog_id,
            author_id=request.user.id,
            rate=rate_value
        )
            
        except Blog.DoesNotExist:
            return JsonResponse({
                'success': False,
                'error': 'Không tìm thấy bài viết.'
            })
            
        return JsonResponse({
            'success': True,
            'message': 'Cảm ơn bạn đã đánh giá!'
        })
    
    
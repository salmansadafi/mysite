from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.
def blog_view(request):
    posts=Post.objects.filter(status=1,published_date__lte=timezone.now())
    context={'posts':posts} 
    return render(request, 'blog/blog-home.html',context)


def blog_single_view(request,pid):
    post = get_object_or_404(Post, id=pid,status=1 ,published_date__lte=timezone.now())
    post.counted_views += 1
    post.save(update_fields=['counted_views'])
    prev_post = Post.objects.filter(status=1,published_date__lte=timezone.now(),id__lt=post.id).order_by('id').last()
    next_post = Post.objects.filter(status=1,published_date__lte=timezone.now(),id__gt=post.id).order_by('id').first()
    context = {
        'post':post,
        'prev_post':prev_post,
        'next_post':next_post}
    return render(request, 'blog/blog-single.html',context)


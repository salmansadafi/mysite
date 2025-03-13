from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.
def blog_view(request):
    posts=Post.objects.filter(published_date__lte=timezone.now())
    context={'posts':posts} 
    return render(request, 'blog/blog-home.html',context)

def blog_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, published_date__lte=timezone.now())

    post.counted_views += 1
    post.save(update_fields=['counted_views'])
    context={'post':post}
    return render(request, 'test.html',context)


def blog_single_view(request):
    context = {'title':'bitcoin price','content':'a content for a test','author':'salmansadafi'}
    return render(request, 'blog/blog-single.html',context)

def test(request,pid):
    post=get_object_or_404(Post, id=pid)
    context={'post':post} 
    return render(request, 'test.html',context)
from django.shortcuts import render
from blog.models import Post

# Create your views here.
def blog_view(request):
    posts=Post.objects.filter(status=1)
    context={'posts':posts} 
    return render(request, 'blog/blog-home.html',context)

def blog_single_view(request):
    context = {'title':'bitcoin price','content':'a content for a test','author':'salmansadafi'}
    return render(request, 'blog/blog-single.html',context)

def test(request):
    posts=Post.objects.all()
    context={'posts':posts} 
    return render(request, 'test.html',context)
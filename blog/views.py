from django.shortcuts import render, get_object_or_404,redirect
from blog.models import Post,Comment
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def blog_view(request,**kwargs):
    posts=Post.objects.filter(status=1,published_date__lte=timezone.now())
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name=kwargs['tag_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username']) # author__username --> because author is a foreign key and it is related to user

    posts = Paginator(posts, 3) # 3 posts per page
    try:
        page_number = request.GET.get('page') # get the page number
        posts = posts.get_page(page_number) # get the current page
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context={'posts':posts} 
    return render(request, 'blog/blog-home.html',context)


def blog_single_view(request,pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Comment submitted successfully')
        else:
            messages.error(request,'Comment not submitted')
    post = get_object_or_404(Post, id=pid,status=1 ,published_date__lte=timezone.now())
    if not post.login_require or request.user.is_authenticated:
        comments = Comment.objects.filter(post=post.id,approved=True)
        form = CommentForm()
        post.counted_views += 1
        post.save(update_fields=['counted_views'])
        prev_post = Post.objects.filter(status=1,published_date__lte=timezone.now(),id__lt=post.id).order_by('id').last()
        next_post = Post.objects.filter(status=1,published_date__lte=timezone.now(),id__gt=post.id).order_by('id').first()
        context = {
            'post':post,
            'comments':comments,
            'form':form,
            'prev_post':prev_post,
            'next_post':next_post}
        return render(request, 'blog/blog-single.html',context)
    else:
        return redirect(reverse('accounts:login'))


def blog_search(request):
    posts=Post.objects.filter(status=1,published_date__lte=timezone.now())
    if request.method == 'GET':
        if s:= request.GET.get('s'): # python walrus
            posts = posts.filter(content__contains=s)
    context={'posts':posts}
    return render(request, 'blog/blog-home.html',context)


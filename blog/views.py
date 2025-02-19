from django.shortcuts import render

# Create your views here.
def blog_view(request):
    return render(request, 'blog/blog-home.html')

def blog_single_view(request):
    context = {'title':'bitcoin price','content':'a content for a test','author':'salmansadafi'}
    return render(request, 'blog/blog-single.html',context)
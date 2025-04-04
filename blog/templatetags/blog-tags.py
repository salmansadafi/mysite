from django import template
from blog.models import Post,Category,Comment
import django.utils.timezone as timezone
register = template.Library()


@register.inclusion_tag('blog/blog-popular-post.html')
def latest_post(arg=3):
    posts=Post.objects.filter(status=1,published_date__lte=timezone.now()).order_by('-published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-category.html')
def post_category():
    posts=Post.objects.filter(status=1)
    categories=Category.objects.all()
    cat_dict= {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}


@register.simple_tag(name='comment_count')
def comment_count(pid):
    return Comment.objects.filter(post=pid,approved=True).count()


    
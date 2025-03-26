from django import template
from blog.models import Post
import django.utils.timezone as timezone
register = template.Library()

@register.inclusion_tag('website/website-latest-post.html')
def latest_post(arg=6):
    posts=Post.objects.filter(status=1,published_date__lte=timezone.now()).order_by('-published_date')[:arg]
    return {'posts':posts}
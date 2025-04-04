from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.utils import timezone

from blog.models import Post


class RssTutorialsFeeds(Feed):
    title = "newest posts"
    link = "/rss/feed"
    description = "a blog for every one"

    def items(self):
        return Post.objects.filter(status=1,published_date__lte=timezone.now())

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)

    def item_lastupdated(self, item):
        return item.updated_at
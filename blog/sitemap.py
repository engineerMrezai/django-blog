from django.contrib.sitemaps import Sitemap
from django.utils import timezone

from .models import *

class BlogSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return Post.objects.filter(status=1, published_date__lte=timezone.now())

    def lastmod(self, obj):
        return obj.published_date
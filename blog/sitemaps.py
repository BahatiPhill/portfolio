from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import BlogArticles

class StaticViewSitemap(Sitemap):

    def items(self):
        return ['home','blog', 'contacts']

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return BlogArticles.objects.filter(publish=True)

    def lastmod(self, obj):
        return obj.timestamp
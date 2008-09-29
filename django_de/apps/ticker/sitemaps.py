from django.contrib.sitemaps import Sitemap
from django_de.apps.ticker.models import Entry

class TickerSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.6

    def items(self):
        return Entry.objects.public()

    def lastmod(self, obj):
        return obj.modified

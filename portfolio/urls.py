
from django.contrib import admin
from django.urls import path, include
from blog.views import home, contacts, DASH
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap

from blog.views import  ArticlesList, ArticlesDetails
from blog.sitemaps import StaticViewSitemap, BlogSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'articles': BlogSitemap
}

urlpatterns = [
    #SiteMaps
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),

    #path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', home, name='home'),
    path('blog/', include('blog.urls')),
    path('contacts/', contacts, name='contacts'),

    #Robot.txt
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),

    #administration
    path('dash/', DASH, name='dash'),

    #API
    path('api/', ArticlesList.as_view()),
    path('api/<slug:slug>/', ArticlesDetails.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

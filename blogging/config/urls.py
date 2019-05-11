from django.contrib import admin

from django.contrib.sitemaps.views import sitemap

from django.urls import path, include

from django.conf import settings

from django.conf.urls.static import static

from blogs.sitemaps import PostSiteMap

sitemaps = {"posts": PostSiteMap}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('blogs/', include('blogs.urls', namespace='blogs')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps },
        name="django.contrib.sitemaps.views.sitemap"),
    path('', include('pages.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

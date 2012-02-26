from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
import nexus

from django.contrib import admin
admin.autodiscover()
nexus.autodiscover()

urlpatterns = patterns('',
    url(r'', include('privatebeta.urls')),
    url(r'', include('app.rm.urls')),    
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^nexus/', include(nexus.site.urls)),
    url(r'^impersonate/', include('impersonate.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
    url(r'', include('social_auth.urls')),
)

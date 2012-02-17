from django.conf import settings
from django.conf.urls import patterns, include, url

from gw.apps.core.views import LocationsView

urlpatterns = patterns('',
    url(r'^$', LocationsView.as_view(), name='home'),
    url(r'^locations_autocomplete/$', "gw.apps.core.views.locations_autocomplete", name='locations_autocomplete'),
)

urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
)

urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
)

import os
from django.conf.urls.defaults import *
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
    #(r'^wikihub/', include('wikihub.wiki.urls')),
    (r'^wikihub/(?P<page_name>[^/]*)/edit/$', 'wikihub.wiki.views.edit_page'),
    (r'^wikihub/(?P<page_name>[^/]*)/save/$', 'wikihub.wiki.views.save_page'),
    (r'^wikihub/(?P<page_name>[^/]*)/$', 'wikihub.wiki.views.view_page'),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root)
)

if settings.DEBUG:
  urlpatterns += patterns('',
      (r'^media/(.*)$', 'django.views.static.serv', {'document_root': os.path.join(settings._DIRNAME, '..', 'media')}),
  )


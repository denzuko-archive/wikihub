from django.conf.urls.defaults import *
from wikihub import settings

import datetime

urlpatterns = patterns('',
    (r'^wikihub/(?P<page_name>[^/]*)/edit/$', 'wikihub.wiki.views.edit_page'),
    (r'^wikihub/(?P<page_name>[^/]*)/save/$', 'wikihub.wiki.views.save_page'),
    (r'^wikihub/(?P<page_name>[^/]*)/$', 'wikihub.wiki.views.view_page')
)

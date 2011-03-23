import django
from django.conf import settings
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import os

from notepad.views import index, profile
#from django.contrib.auth.views import logout

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^gtdnotepad/', include('gtdnotepad.foo.urls')),
    (r'^$',index),
    (r'^accounts/profile/$',profile),
    
    (r'^auth/', include( 'netauth.urls')),
    (r'^api/', include('gtdnotepad.api.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_PATH, 'static')}),
)

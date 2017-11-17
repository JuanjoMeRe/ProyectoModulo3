"""
Definition of urls for VideogamesCodex.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^show\/(?P<id>[0-9]+)$', app.views.show_game),
    url(r'^create\/{0,1}$', app.views.create_game),
    url(r'^edit\/(?P<id>[0-9]+)$', app.views.edit_game),
    url(r'^remove\/(?P<id>[0-9]+)$', app.views.remove_game),
    url(r'^ranking\/{0,1}$', app.views.ranking),


     url(r'', app.views.not_found),
  
 

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]

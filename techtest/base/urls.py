__author__ = 'oerb'

from django.conf.urls import patterns, url
from django.contrib import admin
from views import main_page
admin.autodiscover()

urlpatterns = patterns('',
    # Login Forms
    #url(r'^login/$', 'menues.views.login_page',
    #    name="login"),
    #url(r'^logout/$', 'menues.views.logout_view',
    #    name="logout"),
    # Meta Infos etc.
    #url(r'^impressum/$', 'menues.views.impressum', name='impressum'),
    url(r'^index.html', main_page, name='base/main_page')
)

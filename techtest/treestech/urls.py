__author__ = 'oerb'

from django.conf.urls import patterns, url
from django.contrib import admin
from views import tree1
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^tree1', tree1, name='treestech/tree1')
)

__author__ = 'Marcos'
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^login/$', 'stock.views.login'),
    url(r'^$', 'stock.views.index'),
)
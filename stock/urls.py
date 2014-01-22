__author__ = 'Marcos'
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'', 'stock.views.index'),
)
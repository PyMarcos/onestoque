__author__ = 'Marcos'
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^login/$', 'stock.views.login'),
    url(r'^$', 'stock.views.index'),
    url(r'^test/$', 'stock.views.test_face'),
    url(r'^ajax/$', 'stock.views.ajax'),
    url(r'^produto/$', 'stock.views.gerar_produtos')
)
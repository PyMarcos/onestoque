# -*- coding:utf8 -*-
__author__ = 'Marcos'

from django.conf.urls import patterns, url
from app.views import ProdutoView


urlpatterns = patterns('app.views',
    url(r'^compras/$', 'cons_compras'),
    url(r'^departamentos/$', 'dep'),
    url(r'^departamentos/(?P<dept>.+)/$', 'depts'),
    url(r'^produtos/(?P<order>.*)$', ProdutoView.as_view()),
)

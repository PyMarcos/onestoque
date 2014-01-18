# -*- coding:utf8 -*-
__author__ = 'Marcos'

from django.conf.urls import patterns, url

urlpatterns = patterns('app.views',
    url(r'^contato/$', 'contato'),
    url(r'^novo-produto/$', 'n_produto'),
    url(r'^novo-dep/$', 'n_departamento'),
    url(r'^compra/$', 'n_compra'),
    url(r'^venda/$', 'n_venda'),
)
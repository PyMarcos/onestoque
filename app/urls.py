# -*- coding:utf8 -*-
__author__ = 'Marcos'

from django.conf.urls import patterns, url
from app.views import *


#consultas
urlpatterns = patterns('',
    # consultas
    url(r'^vendas/$', ConsultaVendas.as_view()),
    url(r'^compras/$', ConsultaCompras.as_view()),
    url(r'^departamentos/$', ConsultaDepartamentos.as_view()),
    url(r'^produtos/$', ConsultaProdutos.as_view()),
    url(r'^detalhes/departamentos/(?P<dept>.+)/$', DetalhesDepartamento.as_view()),

    # cadastros
    url(r'^novo_produto/$', NovoProduto.as_view()),
    url(r'^novo_departamento/$', NovoDepartamento.as_view()),
    url(r'^nova_compra/$', NovaCompra.as_view()),
    url(r'^nova_venda/$', NovaVenda.as_view()),

    # commom
    url(r'^$', Index.as_view()),
    url(r'^contato/$', Contato.as_view()),
    url(r'^email/$', EnviarEmail.as_view()),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url':'/login/'}, name='logout'),
)
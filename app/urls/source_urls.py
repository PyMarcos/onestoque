# -*- coding:utf8 -*-
__author__ = 'Marcos'

from django.conf.urls import patterns, include, url
import app.urls.auth_urls as auth_urls
import app.urls.cadastros as cadastros
import app.urls.consultas as consultas
import app.urls.common_urls as common_urls

urlpatterns = patterns(
    url(r'', include(auth_urls)),
    url(r'', include(common_urls)),
    url(r'^consultas/', include(consultas)),
    url(r'^cadastros/', include(cadastros)),
)
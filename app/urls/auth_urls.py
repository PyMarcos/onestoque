# -*- coding:utf8 -*-
__author__ = 'Marcos'

from django.conf.urls import patterns, url

urlpatterns = patterns('app.views',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url':'/login/'}),
)
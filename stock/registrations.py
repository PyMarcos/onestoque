# -*- coding:utf8 -*-
__author__ = 'Marcos'

from stock.models import *
from stock.admin.admin_models import *
from django.contrib import admin

admin.site.register(Product, ProductAdmin)

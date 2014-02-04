# -*- coding:utf8 -*-
__author__ = 'Marcos'

from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline

from stock.models import *

class AddressInline(TabularInline):
    model = Address
    extra = 0

class FedstockInline(TabularInline):
    model = Feedstock
    extra = 0

class ProviderAdmin(ModelAdmin):
    inlines = (AddressInline,)

class CustomerAdmin(ModelAdmin):
    inlines = (AddressInline,)

class PurchaseAdmin(ModelAdmin):
    search_fields = ['date']

class SaleAdmin(ModelAdmin):
    search_fields = ['product']

class FinishedProductAdmin(ModelAdmin):
    filter_vertical = ('feedstocks', )

admin.site.register(FinishedProduct)
admin.site.register(Feedstock)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Sale, SaleAdmin)

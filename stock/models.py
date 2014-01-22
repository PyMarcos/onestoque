# -*- coding:utf8 -*-
from django.db.models import Model
from django.db.models import CharField
from django.db.models import BooleanField
from django.db.models import TextField
from django.db.models import IntegerField
from django.db.models import DecimalField
from django.db.models import DateTimeField
from django.db.models import ForeignKey

from django.contrib.auth.models import User


class StockBaseModel(Model):
    is_active = BooleanField(verbose_name='ativo')

    class Meta:
        abstract = True
        app_label = 'stock'

class Product(StockBaseModel):
    name = CharField(max_length=100, verbose_name='nome')
    quantity = IntegerField()
    price = DecimalField(max_digits=100, decimal_places=3, verbose_name='preço')
    description = TextField()

    class Meta(StockBaseModel.Meta):
        verbose_name = 'produto'


class Partner(StockBaseModel):
    name = CharField(max_length=100, verbose_name='nome')
    phone = CharField(max_length=25, verbose_name='telefone')

class Provider(Partner):
    CNPJ = CharField(max_length=20, verbose_name='CNPJ')

    class Meta(StockBaseModel.Meta):
        verbose_name = 'fornecedor'
        verbose_name_plural = 'fornecedores'

class Customer(Partner):
    cellphone = CharField(max_length=25, verbose_name='celular')
    CPF = CharField(max_length=20, verbose_name='CPF')

    class Meta(StockBaseModel.Meta):
        verbose_name = 'cliente'

class Address(StockBaseModel):
    street = CharField(max_length=100, verbose_name='rua')
    city = CharField(max_length=100, verbose_name='cidade')
    state = CharField(max_length=100, verbose_name='estado')
    district = CharField(max_length=100, verbose_name='bairro')
    number = IntegerField()
    complement = CharField(max_length=100, verbose_name='complemento')
    partner = ForeignKey(Partner)

    class Meta(StockBaseModel.Meta):
        verbose_name = 'endereço'

class Transaction(StockBaseModel):
    user = ForeignKey(User, verbose_name='usuário')
    product = ForeignKey(Product, verbose_name='produto')
    quantity = IntegerField(verbose_name='quantidade')
    total_price = DecimalField(max_digits=100, decimal_places=3, verbose_name='valor total')
    unit_price = DecimalField(max_digits=100, decimal_places=3, verbose_name='valor da unidade')
    date = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name = 'transação'
        verbose_name_plural = 'transações'


class Sale(Transaction):
    customer = ForeignKey(Customer, verbose_name='cliente')

    class Meta(StockBaseModel.Meta):
        verbose_name = 'venda'

class Purchase(Transaction):
    provider = ForeignKey(Provider, verbose_name='fornecedor')

    class Meta(StockBaseModel.Meta):
        verbose_name = 'compra'
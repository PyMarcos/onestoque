from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

class Produto(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        pass

    class Admin(admin.ModelAdmin):
        list_display = ('nome', 'quantidade', 'departamentos')

    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    departamentos = models.ForeignKey('Departamento')

class Departamento(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        pass

    class Admin(admin.ModelAdmin):
        list_display = ('nome',)

    nome = models.CharField(max_length=100)


class Compra(models.Model):
    def __str__(self):
        return self.usuario

    class Meta:
        pass

    class Admin(admin.ModelAdmin):
        list_display = ('usuario', 'produto', 'valor', 'qtd')

    usuario = models.ForeignKey(User, related_name='user_compras')
    produto = models.ForeignKey(Produto, related_name='pr_compras')
    valor = models.FloatField()
    qtd = models.IntegerField()

class Venda(models.Model):
    class Meta:
        pass

admin.site.register(Compra, Compra.Admin)
admin.site.register(Produto, Produto.Admin)
admin.site.register(Departamento, Departamento.Admin)
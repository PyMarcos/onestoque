from time import strftime
from django.db.models import Model
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import IntegerField
from django.db.models import ForeignKey
from django.db.models import DecimalField
from django.db.models import DateTimeField


from django.contrib.auth.models import User
from django.contrib import admin


# Create your models here.

class BaseModel(Model):
    is_active = BooleanField()
    class Meta:
        app_label = 'app'

class Departamento(Model):
    nome = CharField(max_length=100)

    def __unicode__(self):
        return self.nome

    class Meta:
        pass

    class Admin(admin.ModelAdmin):
        list_display = ('nome',)

class Produto(Model):
    nome = CharField(max_length=100)
    quantidade = IntegerField()
    departamentos = ForeignKey('Departamento')

    def __unicode__(self):
        return self.nome

    class Meta:
        pass

    class Admin(admin.ModelAdmin):
        list_display = ('nome', 'quantidade', 'departamentos')

class Compra(Model):
    usuario = ForeignKey(User)
    produto = ForeignKey(Produto)
    valor = DecimalField(decimal_places=2, max_digits=10)
    qtd = IntegerField()
    data = DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'{} - {}'.format(self.usuario, self.data.isoformat())

    class Meta:
        verbose_name = 'compra'

    class Admin(admin.ModelAdmin):
        list_display = ('usuario', 'produto', 'valor', 'qtd')

class Venda(Model):
    usuario = ForeignKey(User)
    produto = ForeignKey(Produto)
    valor = DecimalField(decimal_places=2, max_digits=10)
    qtd = IntegerField()
    data = DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.usuario

admin.site.register(Compra)
admin.site.register(Produto, Produto.Admin)
admin.site.register(Departamento, Departamento.Admin)
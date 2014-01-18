from django import forms
from app.models import *

class FormProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nome', 'quantidade', 'departamentos')

class FormDepartamento(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ('nome',)

class FormCompra(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ('produto', 'valor', 'qtd')

class FormEmail(forms.Form):
    email = forms.CharField(max_length=100)
    assunto = forms.CharField(max_length=100)
    mensagem = forms.CharField(max_length=500)
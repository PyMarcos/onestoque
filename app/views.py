from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.context_processors import csrf
from django.utils.decorators import method_decorator
from django.views.generic import View, ListView
from app.forms import *
from app.funcoes import enviarEmail


class BaseView(View):
    context = {}

class Index(BaseView):
    def get(self, request, *args, **kwargs):
        return render_to_response('home.html', self.context, RequestContext(request))

class Contato(BaseView):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render_to_response('contato.html', self.context, RequestContext(request))

class NovoProduto(BaseView):
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = FormProduto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('salvo.html', self.context, RequestContext(request))

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = FormProduto()
        self.context.update({'form':form, 'tipo':'Produto'})
        return render_to_response('produto.html', self.context, RequestContext(request))

class NovoDepartamento(BaseView):
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = FormDepartamento(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('salvo.html', self.context, RequestContext(request))

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = FormDepartamento()
        self.context.update({'form':form})
        return render_to_response('produto.html', self.context, RequestContext(request))


class NovaCompra(BaseView):
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = FormCompra(request.POST, request.FILES)
        form.usuario = request.user
        if form.is_valid():
            compra = form.save(commit=False)
            compra.usuario = request.user
            compra.save()
            return render_to_response('salvo.html', self.context, RequestContext(request))

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = FormCompra()
        self.context.update({'form':form})
        return render_to_response('produto.html', self.context, RequestContext(request))


class NovaVenda(BaseView):
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = FormCompra(request.POST, request.FILES)
        form.usuario = request.user
        if form.is_valid():
            compra = form.save(commit=False)
            compra.usuario = request.user
            produto = Produto.objects.get(pk=compra.produto.pk)
            produto.quantidade += compra.qtd
            produto.save()
            compra.save()
            return render_to_response('salvo.html', self.context, RequestContext(request))

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = FormCompra()
        self.context.update({'form':form})
        return render_to_response('produto.html', self.context, RequestContext(request))

class ConsultaCompras(BaseView):
    @method_decorator(login_required)
    def get(self, request):
        compras = Compra.objects.filter(usuario=request.user)
        self.context.update({'compras':compras})
        return render_to_response('compras.html', self.context, RequestContext(request))

class ConsultaDepartamentos(BaseView):
    @method_decorator(login_required)
    def get(self, request):
        depts = Departamento.objects.all()
        form = FormDepartamento()
        self.context.update({'depts':depts, 'form':form})
        return render_to_response('produto.html', self.context, RequestContext(request))


class ConsultaProdutos(BaseView):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs ):
        produtos = Produto.objects.all()
        self.context.update({'produtos':produtos})
        return render_to_response('cons-produtos.html', self.context, RequestContext(request))

class ConsultaVendas(BaseView):
    @method_decorator(login_required)
    def get(self, request):
        vendas = Venda.objects.filter(usuario=request.user)
        self.context.update({'compras':vendas})
        return render_to_response('compras.html', self.context, RequestContext(request))

class DetalhesDepartamento(BaseView):
    @method_decorator(login_required)
    def get(self, request):
        dept = Departamento.objects.filter(nome=dept)
        produtos = Produto.objects.filter(departamentos=dept)
        self.context.update({'produtos': produtos})
        return render_to_response('detalhes_departamento.html', self.context, RequestContext(request))

class EnviarEmail(BaseView):
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = FormEmail(request.POST, request.FILES)
            if form.is_valid():
                enviarEmail(form.data)
                return render_to_response('enviado.html')

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = FormEmail()
        self.context.update({'form':form})
        return render_to_response('produto.html', self.context, RequestContext(request))
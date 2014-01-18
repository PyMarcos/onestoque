from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.context_processors import csrf
from django.views.generic import View
from app.forms import *
from app.funcoes import enviarEmail
from django.contrib.auth.forms import forms

def index(request):
    return render_to_response('home.html',{})

@login_required
def contato(request):
    c = {'user': request.user, 'csrf_token':csrf(request)}
    return render_to_response('contato.html', c, context_instance=RequestContext(request))

@login_required
def n_produto(request):
    if request.method == 'POST':
        form = FormProduto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('salvo.html', {})
    else:
        form = FormProduto()
    return render_to_response('produto.html', {'form':form, 'tipo':'Produto'}, context_instance = RequestContext(request))

@login_required
def n_departamento(request):
    if request.method == 'POST':
        form = FormDepartamento(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('salvo.html', {})
    else:
        form = FormDepartamento()
    return render_to_response('produto.html', {'form':form}, context_instance = RequestContext(request))

@login_required
def n_compra(request):
    if request.method == 'POST':
        form = FormCompra(request.POST, request.FILES)
        form.usuario = request.user
        if form.is_valid():
            compra = form.save(commit=False)
            compra.usuario = request.user
            compra.save()
            return render_to_response('salvo.html', {})
    else:
        form = FormCompra()
    return render_to_response('produto.html', {'form':form}, context_instance = RequestContext(request))

@login_required
def n_venda(request):
    if request.method == 'POST':
        form = FormCompra(request.POST, request.FILES)
        form.usuario = request.user
        if form.is_valid():
            compra = form.save(commit=False)
            compra.usuario = request.user
            return render_to_response('salvo.html', {})
    else:
        form = FormCompra()
    return render_to_response('produto.html', {'form':form }, context_instance = RequestContext(request))

@login_required
def cons_compras(request):
    print(request.user)
    compras = Compra.objects.filter(usuario=request.user)
    return render_to_response('compras.html', {'compras':compras})

@login_required
def email(request):
    if request.method == 'POST':
        form = FormEmail(request.POST, request.FILES)
        if form.is_valid():
            enviarEmail(form.data)
            return render_to_response('enviado.html',{})
    else:
        form = FormEmail()
        return render_to_response('email.html', {'form':form}, context_instance = RequestContext(request))

@login_required
def dep(request):
    depts = Departamento.objects.all()
    form = FormDepartamento()
    return render_to_response('dep.html', {'depts':depts, 'form':form}, context_instance = RequestContext(request))

@login_required
def depts(request, dept):
    print dept
    dept = Departamento.objects.filter(nome=dept)
    produtos = Produto.objects.filter(departamentos=dept)
    return render_to_response('prodspordept.html', {'produtos': produtos})

class ProdutoView(View):
    template_name = 'cons-produtos.html'
    produtos = Produto.objects.all()

    def get(self, request, *args, **kwargs ):
        order = kwargs['order']
        if(order):
            self.produtos =  self.produtos.order_by(order)
        return render_to_response(self.template_name, {'produtos':self.produtos}, RequestContext(request))
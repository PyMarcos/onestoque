# -*- coding:utf8 -*-
import urllib
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect

# Create your views here.
from stand import settings
from stock.models import Product


@login_required
def index(request):
    return render_to_response("home.html")

def login(request):
    return render_to_response("login.html")

def test_face(request):
    args = dict(client_id=settings.FACEBOOK_APP_ID, redirect_uri='http://127.0.0.1:8000/')
    return redirect("https://graph.facebook.com/oauth/authorize?" + urllib.urlencode(args))
    return HttpResponse('asdasdasd')

def ajax(request):
    if request.is_ajax():
        products = Product.objects.all()
        JSONresponse = serialize('json', products)
        return HttpResponse(JSONresponse, mimetype='text/javascript')
    return redirect('/')

def gerar_produtos(request):

    Product.objects.create(is_active=True, name='dasdasjdla', quantity=100, price=2.2, description='sadasdasdasd', request_point=60)
    Product.objects.create(is_active=True, name='ssssssssss', quantity=100, price=1.2, description='sadasdasdasd', request_point=60)
    return redirect('/')
# -*- coding:utf8 -*-
from django.shortcuts import render_to_response

# Create your views here.

def index(request):
    return render_to_response("home.html")

def login(request):
    return render_to_response("login.html")
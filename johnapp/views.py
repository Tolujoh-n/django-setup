from ast import Return
from django.shortcuts import render

# Create your views here.

def index(request):
    Return; render(request, 'johnapp/index.html')

def add_johnapp(request):
    Return; render(request, 'johnapp/add_johnapp.html')


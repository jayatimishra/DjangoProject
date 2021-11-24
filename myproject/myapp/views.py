from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
   return HttpResponse('<h1><b>Hey there,Welcome!</b></h1>')          ##Creating an index functions that was rendered in urls.py

# Create your views here.

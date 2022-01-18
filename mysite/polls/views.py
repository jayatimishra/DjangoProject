from re import S
from django.shortcuts import render

from django.http import HttpResponse


def index(request) :
    
    return HttpResponse("Hello, world. You're at the polls index.")
#This is the simplest view possible in Django
#Tocall the view, we need to map to a URL and for this we need a URLConf
#To create URLConf in the polls directory create a urls.py in the polls directory
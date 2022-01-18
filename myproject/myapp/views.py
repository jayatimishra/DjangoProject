from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
   context = "Temp = {0} *C".format(sensor.read_temperature)
   return render(request, 'index.html', {"context": context})


# Create your views here.
##Render request index.html in views.py because views.py knows where to look for the index.html (in the templates folder)"Temp = {0} *C".format(sensor.read_temperature)
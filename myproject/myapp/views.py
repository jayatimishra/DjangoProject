from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
   context = { 'name': 'Jayati',
   'age' : 19, 'nationality' : 'Indian'

   }
   return render(request,'index.html' , context)          ##Creating an index functions that was rendered in urls.py


# Create your views here.
##Render request index.html in views.py because views.py knows where to look for the index.html (in the templates folder)
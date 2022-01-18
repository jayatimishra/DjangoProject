"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/',include('polls.urls')),
    path('admin/', admin.site.urls),
]
#This step is used to point the root URLConf to the polls.urls module 
#The include function allows referencing other URLconfs
#Whenever Django encounters include() it chops off whatever part of the url matched up to that point  and sends the remaining URL to URLconf for further processing
#The idea behing include() is to make it easy to plug-and-play URLs
#Since polls are in their URLconf(polls/urls.py), they can be placed under "/polls/", or nder "/fun_polls/" , or under "/content/polls/", or any other path root and the app will still work.
""" An index view has now been wired to URLconf. We can verify that it's working by running python manage.py runserver




"""
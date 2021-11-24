from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='index')

]  ## This list will take all the urls in our project. path() specifies the urls in the urlspattern list and the '' is the root url, we can add '/download' in it to add another url that can be reached by cicking some button on the website of the root url.

from . import views
from django.urls import path, include
# this is where the url will be
urlpatterns =[
 path('home',  views.home, name='home')
 
]
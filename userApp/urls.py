from . import views
from django.urls import path, include
# this is where the url will be
urlpatterns =[
 path('home',  views.home, name='home'),
 path('edit/<int:id>/', views.editItem, name='edit'),
 path('delete/<int:id>/', views.delItem, name='delete'),
 path('check',views.checking, name='assigns'),
 path('userplus', views.addUser, name='userplus'),
 path('see/<str:added_by>/', views.detailView, name='see')
]
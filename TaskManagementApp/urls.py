from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.intro,name='intro'),
    path('home/', views.homeapp,name='homeapp'),
    path('', views.Logout,name='logout'),
    path('delete/<list_id>', views.delete,name='delete'),
    path('email/', views.email,name='email'),
]

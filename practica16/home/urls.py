from django.urls import path
from . import views

urlpatterns =[
    path('',views.mostrar_pagina,name='home')
]
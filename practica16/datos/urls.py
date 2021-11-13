from django.urls import path
from . import views

urlpatterns =[
    path('',views.datos_pagina,name='datos'),
]
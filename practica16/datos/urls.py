from django.urls import path
from . import views

urlpatterns =[
    path('',views.datos_,name='datos_'),
]
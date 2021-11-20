from django.shortcuts import render

# Create your views here.

def home_pagina(r):
    return render(r,"home.html")
    pass
from django.shortcuts import render, redirect
from django.db import connection

def principal(request):
    return render (request, 'home.html')

def mision(request):
    return render (request, 'mision.html')

def vision(request):
    return render (request, 'vision.html')

def insertar(request):
    return render (request, 'insertar.html')
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def armario(request):
    return render(request, 'armario.html')
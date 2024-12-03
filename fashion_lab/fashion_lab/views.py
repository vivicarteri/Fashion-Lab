from django.shortcuts import render, redirect
from .models import Partes_de_Cima, Partes_de_Baixo, Calçados, Acessórios
from .forms import PartesDeCimaForm, PartesDeBaixoForm, CalcadosForm, AcessoriosForm

def home(request):
    return render(request, 'home.html')

def armario(request):
    return render(request, 'armario.html')

def cadastra_parte_de_cima(request):
    if request.method == "POST":
        form = PartesDeCimaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PartesDeCimaForm()
    return render(request, 'cadastrar_parte_de_cima.html', {'form': form})

def cadastra_parte_de_baixo(request):
    if request.method == 'POST':
        form = PartesDeBaixoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PartesDeBaixoForm()
    return render(request, 'cadastrar_parte_de_baixo.html', {'form': form})

def cadastra_calçado(request):
    if request.method == 'POST':
        form = CalcadosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CalcadosForm()
    return render(request, 'cadastrar_calçado.html', {'form': form})

def cadastra_acessorio(request):
    if request.method == 'POST':
        form = AcessoriosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AcessoriosForm()
    return render(request, 'cadastrar_acessorio.html', {'form': form})
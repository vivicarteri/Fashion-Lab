from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Usuario, Partes_de_Cima, Partes_de_Baixo, Calçados, Acessórios
from .forms import CadastroUsuarioForm, PartesDeCimaForm, PartesDeBaixoForm, CalcadosForm, AcessoriosForm

def home(request):
    return render(request, 'home.html')

@login_required
def armario(request):
    partes_de_cima = Partes_de_Cima.objects.filter(usuario=request.user)
    partes_de_baixo = Partes_de_Baixo.objects.filter(usuario=request.user)
    calçados = Calçados.objects.filter(usuario=request.user)
    acessórios = Acessórios.objects.filter(usuario=request.user)

    return render(request, 'armario.html', {
        'partes_de_cima': partes_de_cima,
        'partes_de_baixo': partes_de_baixo,
        'calçados': calçados,
        'acessórios': acessórios,
    })

def pergunta(request):
    return render(request, 'pergunta.html')

def cadastro_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["usuario"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["senha"]
            )
        
            usuario = Usuario.objects.create(
                    user=user,
                    nome=form.cleaned_data["nome"],
                    genero=form.cleaned_data["genero"],
                    cpf=form.cleaned_data["cpf"],
                    data_nascimento=form.cleaned_data["data_nascimento"]
            )
            return redirect('home')
        else:
            return render(request, 'cadastro_usuario.html', {'form': form})
    
    else:
        form = CadastroUsuarioForm()
    
    return render(request, 'cadastro_usuario.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        user = authenticate(
            username = request.POST["username"],
            password = request.POST["password"]
        )

        if user is not None:
            login(request, user)
            usuario = Usuario.objects.get(user=user)
            return redirect('home')
        else:
            return render(request, 'login_usuario.html', context = {"error_msg": "Usuário não existe"})
    return render(request, 'login_usuario.html')

def logout_usuario(request):
    logout(request)
    return redirect('home')

def pergunta_peca(request, tipo, id):
    if tipo == 'parte_de_cima':
        parte = Partes_de_Cima.objects.get(id=id)
    elif tipo == 'parte_de_baixo':
        parte = Partes_de_Baixo.objects.get(id=id)
    elif tipo == 'calcado':
        parte = CalcadosForm.objects.get(id=id)
    elif tipo == 'acessorio':
        parte = AcessoriosForm.objects.get(id=id)
    return render(request, 'pergunta_peca.html', {'tipo': tipo, 'parte': parte})

def cadastrar_uso(request):
    return render(request, 'cadastrar_uso.html')

def cadastra_parte_de_cima(request):
    if request.method == "POST":
        form = PartesDeCimaForm(request.POST, request.FILES)
        if form.is_valid():
            parte_de_cima = form.save(commit=False)
            parte_de_cima.usuario = request.user
            parte_de_cima.save()
            return redirect('armario') 
    else:
        form = PartesDeCimaForm()
    return render(request, 'cadastrar_parte_de_cima.html', {'form': form})

def parte_de_cima(request, id):
    parte_de_cima = Partes_de_Cima.objects.get(id=id)
    return render(request, 'parte_de_cima.html', {'parte_de_cima': parte_de_cima})

def parte_de_baixo(request, id):
    parte_de_baixo = Partes_de_Baixo.objects.get(id=id)
    return render(request, 'parte_de_baixo.html', {'parte_de_baixo': parte_de_baixo})

def calcado(request, id):
    calcado = Calçados.objects.get(id=id)
    return render(request, 'calcado.html', {'calcado': calcado})

def acessorio(request, id):
    acessorio = Acessórios.objects.get(id=id)
    return render(request, 'acessorio.html', {'acessorio': acessorio})

def cadastra_parte_de_baixo(request):
    if request.method == 'POST':
        form = PartesDeBaixoForm(request.POST, request.FILES)
        if form.is_valid():
            parte_de_baixo = form.save(commit=False)
            parte_de_baixo.usuario = request.user
            parte_de_baixo.save()
            return redirect('armario') 
    else:
        form = PartesDeBaixoForm()
    return render(request, 'cadastrar_parte_de_baixo.html', {'form': form})

def cadastra_calçado(request):
    if request.method == 'POST':
        form = CalcadosForm(request.POST, request.FILES)
        if form.is_valid():
            calcado = form.save(commit=False)
            calcado.usuario = request.user
            calcado.save()
            return redirect('armario') 
    else:
        form = CalcadosForm()
    return render(request, 'cadastrar_calçado.html', {'form': form})

def cadastra_acessorio(request):
    if request.method == 'POST':
        form = AcessoriosForm(request.POST, request.FILES)
        if form.is_valid():
            acessorio = form.save(commit=False)
            acessorio.usuario = request.user
            acessorio.save()
            return redirect('armario') 
    else:
        form = AcessoriosForm()
    return render(request, 'cadastrar_acessorio.html', {'form': form})
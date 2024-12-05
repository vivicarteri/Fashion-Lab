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
    return render(request, 'armario.html')

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
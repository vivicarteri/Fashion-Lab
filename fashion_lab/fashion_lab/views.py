from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count
from .models import Usuario, Partes_de_Cima, Partes_de_Baixo, Calçados, Acessórios, UsoRoupa
from .forms import CadastroUsuarioForm, PartesDeCimaForm, PartesDeBaixoForm, CalcadosForm, AcessoriosForm, UsoRoupaForm, LookForm

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

    content_type = ContentType.objects.get_for_model(parte)

    return render(request, 'pergunta_peca.html', {
        'tipo': tipo,
        'parte': parte,
        'content_type_id': content_type.id,
    })

def cadastro_uso_roupa(request, roupa_id, content_type_id):
    content_type = ContentType.objects.get(id=content_type_id)
    roupa = content_type.get_object_for_this_type(id=roupa_id)
    estrelas = range(1, 6)

    usos_roupa = UsoRoupa.objects.filter(roupa_content_type=content_type, roupa_object_id=roupa.id)
    ocasião_mais_frequente = usos_roupa.values('ocasiao').annotate(ocasiões_count=Count('ocasiao')).order_by('-ocasiões_count').first()

    if ocasião_mais_frequente:
        ocasião_mais_frequente = ocasião_mais_frequente['ocasiao']

    if request.method == 'POST':
        form = UsoRoupaForm(request.POST)
        if form.is_valid():
            uso_roupa = form.save(commit=False)
            uso_roupa.roupa_content_type = content_type
            uso_roupa.roupa_object_id = roupa.id
            uso_roupa.save()
            return redirect('armario')
    
    else:
        form = UsoRoupaForm()

    return render(request, 'cadastro_uso.html', {
        'form': form,
        'estrelas': estrelas,
        'roupa': roupa,
        'content_type': content_type,
        'ocasião_mais_frequente': ocasião_mais_frequente
    })

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
    
    parte_de_cima_usos = UsoRoupa.objects.filter(
        roupa_content_type=ContentType.objects.get_for_model(Partes_de_Cima),
        roupa_object_id=parte_de_cima.id
    ).order_by('-data_uso')

    ocasião_mais_frequente = parte_de_cima.ocasiao_mais_frequente()

    estrelas = range(1, 6)
    cor_visual = parte_de_cima.cor_visual
    return render(request, 'parte_de_cima.html', {
        'parte_de_cima': parte_de_cima,
        'cor_visual': cor_visual,
        'estrelas': estrelas,
        'parte_de_cima_usos': parte_de_cima_usos,
        'ocasião_mais_frequente': ocasião_mais_frequente,
    })

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

def looks(request):
    partes_de_cima = Partes_de_Cima.objects.filter(usuario=request.user)
    partes_de_baixo = Partes_de_Baixo.objects.filter(usuario=request.user)
    calçados = Calçados.objects.filter(usuario=request.user)
    acessórios = Acessórios.objects.filter(usuario=request.user)

    parte_de_cima_selecionada = None
    parte_de_baixo_selecionada = None
    calcado_selecionado = None

    if request.method == 'POST':
        form = LookForm(request.POST)
        if form.is_valid():
            parte_de_cima_selecionada = form.cleaned_data.get('parte_de_cima')
            parte_de_baixo_selecionada = form.cleaned_data.get('parte_de_baixo')
            calcado_selecionado = form.cleaned_data.get('calcado')

    else:
        form = LookForm()

    return render(request, 'looks.html', {
        'form': form,
        'partes_de_cima': partes_de_cima,
        'partes_de_baixo': partes_de_baixo,
        'calçados': calçados,
        'acessórios': acessórios,
        'parte_de_cima_selecionada': parte_de_cima_selecionada,
        'parte_de_baixo_selecionada': parte_de_baixo_selecionada,
        'calcado_selecionado': calcado_selecionado,
    })
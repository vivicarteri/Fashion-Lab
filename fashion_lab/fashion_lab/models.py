from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    nome = models.CharField(max_length=100)
    genero = models.CharField(
        max_length=50,
        choices=[('feminino', 'Feminino'),
                 ('masculino', 'Masculino'),
                 ('nao-binario', 'Não-binário'),
                 ('outro', 'Outro')]
    )
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Partes_de_Cima(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  imagem = models.ImageField(upload_to='imagens/partes_de_cima/')
  descricao = models.TextField(max_length=100)
  cor = models.CharField(max_length=20)
  marca = models.CharField(max_length=100)
  material = models.CharField(max_length=100)
  tamanho = models.CharField(
    max_length=10,
    choices=[
      ('pp', 'PP'),
        ('p', 'P'),
        ('m', 'M'),
        ('g', 'G'),
        ('gg', 'GG'),
        ('xgg', 'XGG'),
        ('extra_gg', 'Extra GG'),
    ],
  )

  def __str__(self):
    return "%s" % (self.descricao)
  
  class Meta:
        verbose_name = "Parte de Cima"
        verbose_name_plural = "Partes de Cima"

class Partes_de_Baixo(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  imagem = models.ImageField(upload_to='imagens/partes_de_baixo/')
  descricao = models.TextField(max_length=100)
  cor = models.CharField(max_length=20)
  marca = models.CharField(max_length=100)
  material = models.CharField(max_length=100)
  tamanho = models.CharField(max_length=10, 
        choices=[
        ('pp', 'PP (36-38)'),
        ('p', 'P (38-40)'),
        ('m', 'M (40-42)'),
        ('g', 'G (42-44)'),
        ('gg', 'GG (44-46)'),
        ('xgg', 'XGG (46-48)'),
        ('extra_gg', 'Extra GG (48+)'),
    ])
  comprimento = models.CharField(max_length=10, choices=[
        ('curto', 'Curto'),
        ('médio', 'Médio'),
        ('longo', 'Longo'),
    ])

  def __str__(self):
    return "%s" % (self.descricao)
  
  class Meta:
        verbose_name = "Parte de Baixo"
        verbose_name_plural = "Partes de Baixo"

class Calçados(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='imagens/calcados/')
    descricao = models.TextField(max_length=100)
    cor = models.CharField(max_length=20)
    marca = models.CharField(max_length=100)
    material = models.CharField(max_length=100, choices=[ 
        ('borracha', 'Borracha'),
        ('couro', 'Couro'),
        ('plástico', 'Plástico'),
        ('sintético', 'Sintético'),
    ], blank=True, null=True)
    tamanho = models.IntegerField(
        choices=[(i, str(i)) for i in range(33, 47)],
    )
    tipo = models.CharField(max_length=50, choices=[
        ('esportivo', 'Esportivo'),
        ('social', 'Social'),
        ('botas', 'Botas'),
        ('sandália', 'Sandália'),
        ('rasteirinha', 'Rasteirinha'),
        ('sapatilha', 'Sapatilha'),
    ])

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Calçado"
        verbose_name_plural = "Calçados"

class Acessórios(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='imagens/acessorios/')
    descricao = models.TextField(max_length=100)
    cor = models.CharField(max_length=20)
    marca = models.CharField(max_length=100)

    tipo = models.CharField(max_length=50, choices=[
        ('bolsa', 'Bolsa'),
        ('oculos', 'Óculos'),
        ('brinco', 'Brinco'),
        ('colares', 'Colar'),
        ('pulseira', 'Pulseira'),
        ('anel', 'Anel'),
    ])

    tamanho = models.CharField(max_length=50, blank=True, null=True, choices=[
        ('pequeno', 'Pequeno'),
        ('medio', 'Médio'),
        ('grande', 'Grande'),
    ])

    material_acessorio = models.CharField(max_length=100, choices=[
        ('couro', 'Couro'),
        ('tela', 'Tela'),
        ('plástico', 'Plástico'),
        ('metal', 'Metal'),
        ('pedras_preciosas', 'Pedras preciosas'),
        ('sintético', 'Sintético'),
    ])

    def __str__(self):
        return self.descricao
    
    def clean(self):
        super().clean()
        if self.tipo == 'bolsa' and not self.tamanho:
            raise ValidationError({'tamanho': 'Indique o tamanho da sua bolsa!'})
        if self.tipo != 'bolsa' and self.tamanho:
            raise ValidationError({'tamanho': 'Tamanho é válido apenas para bolsas.'})

    class Meta:
        verbose_name = "Acessório"
        verbose_name_plural = "Acessórios"
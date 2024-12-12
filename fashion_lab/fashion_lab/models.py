from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from collections import Counter
from django.contrib.contenttypes.models import ContentType

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
  cor_texto = models.CharField(max_length=20)
  cor_visual = models.CharField(max_length=7, default='#000000')
  marca = models.CharField(max_length=100)
  material = models.CharField(max_length=100)
  tamanho = models.CharField(
    max_length=10,
    choices=[
      ('PP', 'PP'),
        ('P', 'P'),
        ('M', 'M'),
        ('G', 'G'),
        ('GG', 'GG'),
        ('XGG', 'XGG'),
    ],
  )
  usos = GenericRelation('UsoRoupa')

  def __str__(self):
    return "%s" % (self.descricao)
  
  def total_usos(self):
    content_type = ContentType.objects.get_for_model(self)
    return UsoRoupa.objects.filter(roupa_content_type=content_type, roupa_object_id=self.id).count()

  def ocasiao_mais_frequente(self):
    usos = UsoRoupa.objects.filter(
      roupa_content_type=ContentType.objects.get_for_model(Partes_de_Cima),
      roupa_object_id=self.id
        )
    
    ocasiões = [uso.ocasiao for uso in usos]
    if ocasiões:
        return max(set(ocasiões), key=ocasiões.count)
    return None
  
  def media_avaliacoes(self):
    avaliacoes = [uso.avaliacao for uso in self.usos.all()]
    if avaliacoes:
        media = sum(avaliacoes) / len(avaliacoes)
        return round(media)
    return 0
  
  def ultimo_uso(self):
    ultimo_uso = self.usos.order_by('-data_uso').first()
    return ultimo_uso
  
  def delete(self, *args, **kwargs):
        self.uso_roupa.all().delete()
        super().delete(*args, **kwargs)
  
  class Meta:
        verbose_name = "Parte de Cima"
        verbose_name_plural = "Partes de Cima"

class Partes_de_Baixo(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  imagem = models.ImageField(upload_to='imagens/partes_de_baixo/')
  descricao = models.TextField(max_length=100)
  cor_texto = models.CharField(max_length=20)
  cor_visual = models.CharField(max_length=7, default='#000000')
  marca = models.CharField(max_length=100)
  material = models.CharField(max_length=100)
  tamanho = models.CharField(max_length=10, 
        choices=[
        ('PP', 'PP (36-38)'),
        ('P', 'P (38-40)'),
        ('M', 'M (40-42)'),
        ('G', 'G (42-44)'),
        ('GG', 'GG (44-46)'),
        ('XGG', 'XGG (46-48)'),
        ('Extra GG', 'Extra GG (48+)'),
    ])
  comprimento = models.CharField(max_length=10, choices=[
        ('curto', 'Curto'),
        ('médio', 'Médio'),
        ('longo', 'Longo'),
    ])

  def __str__(self):
    return "%s" % (self.descricao)
  
  def total_usos(self):
    return self.usos.count()

  def ocasiao_mais_frequente(self):
    ocasiões = [uso.ocasiao for uso in self.usos.all()]
    return Counter(ocasiões).most_common(1)[0][0] if ocasiões else "Nenhuma"
  
  def media_avaliacoes(self):
    avaliacoes = [uso.avaliacao for uso in self.usos.all()]
    if avaliacoes:
        media = sum(avaliacoes) / len(avaliacoes)
        return round(media)
    return 0
  
  def ultimo_uso(self):
    ultimo_uso = self.usos.order_by('-data_uso').first()
    return ultimo_uso
  
  class Meta:
        verbose_name = "Parte de Baixo"
        verbose_name_plural = "Partes de Baixo"

class Calçados(models.Model):
    
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  imagem = models.ImageField(upload_to='imagens/calcados/')
  descricao = models.TextField(max_length=100)
  cor_texto = models.CharField(max_length=20)
  cor_visual = models.CharField(max_length=7, default='#000000')
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
    
  def total_usos(self):
    return self.usos.count()

  def ocasiao_mais_frequente(self):
    ocasiões = [uso.ocasiao for uso in self.usos.all()]
    return Counter(ocasiões).most_common(1)[0][0] if ocasiões else "Nenhuma"
  
  def media_avaliacoes(self):
    avaliacoes = [uso.avaliacao for uso in self.usos.all()]
    if avaliacoes:
        media = sum(avaliacoes) / len(avaliacoes)
        return round(media)
    return 0
  
  def ultimo_uso(self):
    ultimo_uso = self.usos.order_by('-data_uso').first()
    return ultimo_uso

  class Meta:
    verbose_name = "Calçado"
    verbose_name_plural = "Calçados"

class Acessórios(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  imagem = models.ImageField(upload_to='imagens/acessorios/')
  descricao = models.TextField(max_length=100)
  cor_texto = models.CharField(max_length=20)
  cor_visual = models.CharField(max_length=7, default='#000000')
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
  
  def total_usos(self):
    return self.usos.count()

  def ocasiao_mais_frequente(self):
    ocasiões = [uso.ocasiao for uso in self.usos.all()]
    return Counter(ocasiões).most_common(1)[0][0] if ocasiões else "Nenhuma"
  
  def media_avaliacoes(self):
    avaliacoes = [uso.avaliacao for uso in self.usos.all()]
    if avaliacoes:
        media = sum(avaliacoes) / len(avaliacoes)
        return round(media)
    return 0
  
  def ultimo_uso(self):
    ultimo_uso = self.usos.order_by('-data_uso').first()
    return ultimo_uso
    
  def clean(self):
    super().clean()
    if self.tipo == 'bolsa' and not self.tamanho:
        raise ValidationError({'tamanho': 'Indique o tamanho da sua bolsa!'})
    if self.tipo != 'bolsa' and self.tamanho:
        raise ValidationError({'tamanho': 'Tamanho é válido apenas para bolsas.'})

  class Meta:
    verbose_name = "Acessório"
    verbose_name_plural = "Acessórios"

class UsoRoupa(models.Model):
    roupa_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="usos")
    roupa_object_id = models.PositiveIntegerField()
    roupa = GenericForeignKey('roupa_content_type', 'roupa_object_id')

    data_uso = models.DateField()
    avaliacao = models.IntegerField(choices=[(i, f"{i} estrelas") for i in range(6)])
    ocasiao = models.CharField(max_length=100, choices=[
        ('Trabalho', 'Trabalho'),
        ('Lazer', 'Lazer'),
        ('Festa', 'Festa'),
        ('Casual', 'Casual'),
        ('Formal', 'Formal'),
        ('Outro', 'Outro'),
    ])

    def __str__(self):
        return f"{self.data_uso} - {self.roupa}"
    